# from django.contrib import admin
# from django.db.models import fields
# from django import forms

# # Register your models here.
# from .models import *
# from import_export import resources
# from import_export.fields import Field
# from import_export.admin import ImportExportModelAdmin
# from import_export.forms import ImportForm, ConfirmImportForm

# class CustomShipmentItemForm(ImportForm):
#     shipment = forms.ModelChoiceField(queryset=Shipment.objects.all(), required=True)

# class CustomConfirmShipmentItemForm(ConfirmImportForm):
#     shipment = forms.ModelChoiceField(queryset=Shipment.objects.all(), required=True)

# class ShipmentItemResource(resources.ModelResource):
#     class Meta:
#         models = ShipmentItem
#         fields = ('carpet__design__name', 'carpet__color__primary_color', 'quantity')

# class ShipmentItemAdmin(ImportExportModelAdmin):
#     resource_class = ShipmentItemResource

#     def get_import_form(self):
#         return CustomShipmentItemForm

#     def get_confirm_import_form(self):
#         return CustomConfirmShipmentItemForm

#     def get_form_kwargs(self, form, *args, **kwargs):
#         # pass on `author` to the kwargs for the custom confirm form
#         if isinstance(form, CustomConfirmShipmentItemForm):
#             if form.is_valid():
#                 shipment = form.cleaned_data['shipment']
#                 kwargs.update({'shipment': shipment.id})
#         return kwargs

#     def design_collection(self, obj):
#         return obj.carpet.design.collection.name

# class CarpetResource(resources.ModelResource):
#     size_shape = Field()
#     class Meta:
#         model = Carpet
#         fields = ('design__name', 'color__primary_color', 'size_shape', 'inventory')

#     def dehydrate_size_shape(self, carpet):
#         return '%s x %s %s' % (carpet.size.length, carpet.size.width, carpet.size.shape)

# class CarpetAdmin(ImportExportModelAdmin):
#     resource_class = CarpetResource
#     list_display = ['id', 'image_tag', 'design_collection', 'design', 'color', 'size', 'inventory']
#     list_filter = ['design__collection', 'color', 'size']
#     list_editable = ['inventory']
#     search_fields = ['design__name', 'design__collection__name']
#     def design_collection(self, obj):
#         return obj.design.collection.name

# class CarpetTabularInline(admin.TabularInline):
#     model = Carpet
#     show_change_link = True


# class DesignTabularInline(admin.TabularInline):
#     model = Design
#     show_change_link = True

# class CollectionTabularInline(admin.TabularInline):
#     model = Collection
#     show_change_link = True


# admin.site.register([Color, Size])
# admin.site.register(Carpet, CarpetAdmin) 
# admin.site.register(Design, DesignAdmin)
# admin.site.register(Collection, CollectionAdmin)
# admin.site.register(Brand, BrandAdmin)

# admin.site.register(ShipmentItem, ShipmentItemAdmin)
# admin.site.register([Shipment])
