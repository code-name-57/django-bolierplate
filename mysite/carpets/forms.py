from django import forms
from django.forms import fields
from .models import Carpet, Brand

class CarpetImageForm(forms.ModelForm):
    class Meta:
        model= Carpet
        fields= ["image_file"]

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ["name", "website"]