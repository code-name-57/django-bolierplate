from django.db.models import fields
from django.forms import ModelForm, \
        TextInput, \
        Textarea
from .models import Address, Retailer, Consumer, Order
from django.contrib.auth.models import User
from address.forms import AddressField


class RetailerRegistrationForm(ModelForm):
    class Meta:
        model = Retailer
        fields = ("address","contact_number", "sale_tax_number", "store_name")


class ConsumerRegistrationForm(ModelForm):
    class Meta:
        model = Consumer
        fields = ("address","contact_number")


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class CheckoutForm(ModelForm):
    # address = AddressField()
    class Meta:
        model = Order
        fields = ('card_number',)
