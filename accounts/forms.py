from django.forms import ModelForm, \
        TextInput, \
        Textarea
from .models import Retailer
from django.contrib.auth.models import User


class UserRegistrationForm(ModelForm):
    class Meta:
        model = Retailer
        fields = ("address", "contact_number", "sale_tax_number", "store_name")
        widgets = {
            'display_name': TextInput(),
            'description': Textarea(attrs={'cols': 40, 'rows': 10}),
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')