from django.db import models
from django.contrib.auth.models import User
from address.models import AddressField
from django.db.models.enums import Choices
from django.forms.models import ModelForm
from catalog.models import Carpet
from phonenumber_field.modelfields import PhoneNumberField

class Address(models.Model):
    STATE_CHOICES = (
    ('TX', 'Texas'),
    ('CO', 'Colorado'),
    ('AZ', 'Arizona'),
    )
    country = models.CharField(max_length=20)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    zip_code = models.IntegerField()
    state = models.CharField(max_length=30, choices=STATE_CHOICES, default='TX')

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
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

# TODO Make Item class, which can be derived by cart item and order item
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(default = 0.0, max_digits = 10, decimal_places=2)
    carpet = models.ForeignKey(Carpet, on_delete=models.CASCADE)

class Order(models.Model):
    # TODO Use abbrev for choices. get_status_display() not working currently.
    STATUS_CHOICES = (
    ('RECIEVED', 'RECIEVED'),
    ('QUOTATION SENT', 'QUOTATION SENT'),
    ('PAID', 'PAID'),
    ('SHIPPED', 'SHIPPED'),
    ('DELIVERED', 'DELIVERED'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=15, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'RECIEVED')
    total = models.IntegerField(default = 20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(default = 0.0, max_digits = 10, decimal_places=2)
    carpet = models.ForeignKey(Carpet, on_delete=models.CASCADE)