from django.contrib import admin

# Register your models here.
from .models import *
from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin

class CarpetResource(resources.ModelResource):
    size_shape = Field()
    class Meta:
        model = Carpet
        fields = ('design__name', 'color__primary_color', 'size_shape', 'inventory')

    def dehydrate_size_shape(self, carpet):
        return '%s x %s %s' % (carpet.size.length, carpet.size.width, carpet.size.shape)

class CarpetAdmin(ImportExportModelAdmin):
    resource_class = CarpetResource
    list_display = ['id', 'image_tag', 'design_collection', 'design', 'color', 'size', 'inventory']
    list_filter = ['design__collection', 'color', 'size']
    list_editable = ['inventory']
    search_fields = ['design__name', 'design__collection__name']
    def design_collection(self, obj):
        return obj.design.collection.name

class CarpetTabularInline(admin.TabularInline):
    model = Carpet
    show_change_link = True


class DesignTabularInline(admin.TabularInline):
    model = Design
    show_change_link = True

class CollectionTabularInline(admin.TabularInline):
    model = Collection
    show_change_link = True


class DesignAdmin(admin.ModelAdmin):
    inlines = [CarpetTabularInline]
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

class BrandAdmin(admin.ModelAdmin):
    inlines = [CollectionTabularInline]
    list_display = ['name', 'website']
    search_fields = ['name']

admin.site.register([Color, Size])
admin.site.register(Carpet, CarpetAdmin) 
admin.site.register(Design, DesignAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Brand, BrandAdmin)
