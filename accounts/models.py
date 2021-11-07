from django.db import models
from django.contrib.auth.models import User
from address.models import AddressField
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = AddressField(blank=False)
    contact_number = PhoneNumberField(blank=True)

    class Meta:
        abstract = True


class Retailer(Customer):
    store_name = models.CharField(max_length=100, blank=False)
    sale_tax_number = models.CharField(max_length=20, blank=False)
    is_approved = models.BooleanField(default=False)


class Consumer(Customer):
    is_approved = models.BooleanField(default=True)
