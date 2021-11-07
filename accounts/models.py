from django.db import models
from django.contrib.auth.models import User
from address.models import AddressField
from catalog.models import Carpet
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

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(default = 0.0, max_digits = 10, decimal_places=2)
    carpet = models.ForeignKey(Carpet, on_delete=models.CASCADE)
