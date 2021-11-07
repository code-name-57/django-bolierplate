from django.forms import ModelForm, \
        TextInput, \
        Textarea
from .models import Retailer, Consumer
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