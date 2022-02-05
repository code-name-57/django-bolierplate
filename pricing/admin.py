from dataclasses import field
from django.contrib import admin

from pricing.models import CollectionSize, CollectionSizePrice, PricingPackage, PricingItem

# Register your models here.
class CollectionSizePriceInline(admin.TabularInline):
    fields = ('collectionSize', 'collection_name', 'collection_size', 'price')
    readonly_fields = ('collection_name', 'collection_size')
    model = CollectionSizePrice
    def collection_name(self, obj):
        return obj.collectionSize.collection.name

    def collection_size(self, obj):
        return obj.collectionSize.size


class PricingAdmin(admin.ModelAdmin):
    inlines = (CollectionSizePriceInline, )
    model = PricingPackage

class PricingItem(admin.ModelAdmin):
    model = PricingItem



admin.site.register(PricingPackage, PricingAdmin)
admin.site.register([CollectionSize])