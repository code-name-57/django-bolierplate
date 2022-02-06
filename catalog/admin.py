from django.contrib import admin
from django.db.models.query import QuerySet

# Register your models here.
from .models import *
from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
from django.contrib import messages

from django.utils.safestring import mark_safe

from .utils.image_importer import ImageImporter

from django.contrib.admin.widgets import AdminFileWidget

class AdminImageWidget(AdminFileWidget):

    def render(self, name, value, attrs=None, renderer=None):
        output = []

        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)

            output.append(
                f' <a href="{image_url}" target="_blank">'
                f'  <img src="{image_url}" alt="{file_name}" width="150" height="150" '
                f'style="object-fit: cover;"/> </a>')

        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe(u''.join(output))

class CarpetAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_tag', 'design_collection', 'designColor', 'size', 'inventory']
    list_filter = ['designColor__design__collection', 'designColor__color', 'size']
    list_editable = ['inventory']
    search_fields = ['designColor__design__name', 'designColor__design__collection__name']
    def design_collection(self, obj):
        return obj.designColor.design.collection.name


class CarpetTabularInline(admin.TabularInline):
    model = Carpet
    show_change_link = True


class DesignTabularInline(admin.TabularInline):
    model = Design
    show_change_link = True




class DesignInColorTabularInline(admin.TabularInline):
    model = DesignInColor
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}

    show_change_link = True


class CollectionTabularInline(admin.TabularInline):
    model = Collection
    show_change_link = True


class DesignAdmin(admin.ModelAdmin):
    inlines = [DesignInColorTabularInline]
    list_display = ['name', 'collection']
    list_filter = ['collection', 'collection__brand']
    filter_horizontal = ('available_colors',)
    search_fields = ['name', 'collection__name']

class CollectionAdmin(admin.ModelAdmin):
    inlines = [DesignTabularInline]
    list_display = ['name', 'brand', 'description']
    list_filter = ['brand']
    filter_horizontal = ('available_sizes',)
    search_fields = ['name']

    actions = ['import_images']

    @admin.action(description='Import New Images Folder')
    def import_images(self, request, queryset):
        img_imp = ImageImporter(request, queryset, self)



class BrandAdmin(admin.ModelAdmin):
    inlines = [CollectionTabularInline]
    list_display = ['name', 'website']
    search_fields = ['name']


admin.site.register([Color, Size])
admin.site.register(Carpet, CarpetAdmin) 
admin.site.register(Design, DesignAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Brand, BrandAdmin)
