from enum import unique
from django.db import models
from django.contrib import admin
from django.db.models import constraints
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

from catalog.models import Carpet

# Create your models here.
class Shipment(models.Model):
    manufacturer = models.CharField(max_length=30)
    ordered_date = models.DateField(blank = True)
    arrival_date = models.DateField(blank = True)
    available = models.BooleanField(default=False)
    packing_sheet =  models.FileField(upload_to='shipments/', blank=True)
    processed = models.BooleanField(default=False)
        


class ShipmentItem(Carpet):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, null=True)
    barcode = models.CharField(max_length=30, blank = True)
    quantity = models.PositiveIntegerField(default=1)