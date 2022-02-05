from pyexpat import model
from statistics import mode
from django.db import models

from catalog.models import Collection, Size

# Create your models here.

class CollectionSize(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=False)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=False)

class PricingPackage(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    prices = models.ManyToManyField(CollectionSize, through='CollectionSizePrice')

class CollectionSizePrice(models.Model):
    pricing = models.ForeignKey(PricingPackage, on_delete=models.CASCADE, null=False)
    collectionSize = models.ForeignKey(CollectionSize, on_delete=models.CASCADE, null=False)
    
    price = models.IntegerField(default=0, blank=False, null=False)

class PricingItem(models.Model):
    pricing = models.ForeignKey(PricingPackage, on_delete=models.CASCADE, null=False)

    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=False)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=False)
    price = models.IntegerField(default=0, blank=False, null=False)