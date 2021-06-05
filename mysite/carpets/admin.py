from django.contrib import admin

# Register your models here.
from .models import Brand, Carpet, Color, Collections, Design, Size

admin.site.register([Brand, Collections, Carpet, Color, Design, Size])