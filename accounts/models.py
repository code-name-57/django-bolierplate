from django.db import models
from django.contrib.auth.models import User
from address.models import AddressField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Retailer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=100, blank=False)
    address = AddressField(blank=False)
    sale_tax_number = models.CharField(max_length=20, blank=False)
    contact_number = PhoneNumberField(blank=True)
