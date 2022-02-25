from django.contrib import admin
from django.contrib import messages
from django.db.models import fields
from django.contrib.admin import helpers
from django.template.response import TemplateResponse

from django import forms

# Register your models here.
from .models import *
from .utils import spreadsheet
class ShipmentItemTabularInline(admin.TabularInline):
    model = ShipmentItem
    readonly_fields=['barcode', 'carpet', 'carpet_size', 'quantity']
    extra = 0
    # def carpet
    def carpet_size(self, si):
        return si.carpet.size

class ShipmentAdmin(admin.ModelAdmin):
    inlines = [ShipmentItemTabularInline]
    actions = ['process_packing_sheet', 'mark_as_arrived']

    @admin.action(description='Process Packing Sheet')
    def process_packing_sheet(self, request, queryset):
        if request.POST.get('post'):
            for shipment in queryset:
                print(shipment)
                shipment_created_count = 1
                # shipment_created_count, error = spreadsheet.process_packing_sheet(shipment)
                if(shipment_created_count>0):
                    self.message_user(request, str(shipment_created_count) + " new shipment items creates", messages.SUCCESS)
                else:
                    self.message_user(request, repr(error) + ". Packing list not processed. Please clean the packing sheet", messages.ERROR)
        else:
            context = {
                'title': "Are you sure?",
                'queryset': queryset,
                'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
            }
            return TemplateResponse(request, 'shipment_confirmation.html',
                context)

    @admin.action(description="Mark as arrived")
    def mark_as_arrived(self, request, queryset):
        for shipment in queryset:
            if shipment.available:
                self.message_user(request, str(shipment) + " : Shipment already marked as arrived", messages.WARNING)
            else:
                shipment.available = True
                for shItem in ShipmentItem.objects.filter(shipment=shipment):
                    print(shItem.quantity)
                    shItem.carpet.inventory = shItem.quantity + shItem.carpet.inventory
                    shItem.carpet.save()
                shipment.save()
                self.message_user(request, str(shipment) + " : Shipment marked as arrived succesfully", messages.SUCCESS)

admin.site.register(Shipment, ShipmentAdmin)
admin.site.register([ShipmentItem])
    