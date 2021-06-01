from django import forms
from .models import Carpet

class ImageForm(forms.ModelForm):
    class Meta:
        model= Carpet
        fields= ["name", "image_file"]
