from django.contrib import admin
from django.db.models import fields
from django import forms

# Register your models here.
from .models import *
from .utils import spreadsheet
class ShipmentItemTabularInline(admin.TabularInline):
    model = ShipmentItem
    readonly_fields=['carpet_size', 'quantity']

    # def carpet
    def carpet_size(self, si):
        return si.carpet.size

class ShipmentAdmin(admin.ModelAdmin):
    inlines = [ShipmentItemTabularInline]
    actions = ['process_packing_sheet']

    @admin.action(description='Process Packing Sheet')
    def process_packing_sheet(self, request, queryset):
        for shipment in queryset:
            spreadsheet.process_packing_sheet(shipment)
            

admin.site.register(Shipment, ShipmentAdmin)
admin.site.register([ShipmentItem])
    