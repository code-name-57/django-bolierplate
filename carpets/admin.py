from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register([Brand, Collections, Color, Design, Size])
admin.site.register(Carpet, CarpetAdmin)