from django.contrib import admin

# Register your models here.
from .models import *
from import_export import resources
from import_export.fields import Field

class EnvColorAdmin(admin.ModelAdmin):
    list_display = ['color']

class FloorTextureAdmin(admin.ModelAdmin):
    list_display = ['floortype_name', 'name', 'image_tag']
    def floortype_name(self, obj):
        return obj.floortype.name

class FloorTextureTabularInline(admin.TabularInline):
    model = FloorTexture
    show_change_link = True

class FloorTypeAdmin(admin.ModelAdmin):
    inlines = [FloorTextureTabularInline]
    list_display = ['name']


admin.site.register(EnvColor, EnvColorAdmin)
admin.site.register(FloorTexture, FloorTextureAdmin)
admin.site.register(FloorType, FloorTypeAdmin)