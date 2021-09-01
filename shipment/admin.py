from django.contrib import admin
from django.contrib import messages
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
            shipment_created_count, error = spreadsheet.process_packing_sheet(shipment)
            if(shipment_created_count>0):
                self.message_user(request, str(shipment_created_count) + " new shipment items creates", messages.SUCCESS)
            else:
                self.message_user(request, repr(error) + ". Packing list not processed. Please clean the packing sheet", messages.ERROR)


admin.site.register(Shipment, ShipmentAdmin)
admin.site.register([ShipmentItem])
    