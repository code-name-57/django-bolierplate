from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

from .models import Retailer
# Register your models here.


class RetailerProfileInline(admin.StackedInline):
    model = Retailer

class CustomUserAdmin(UserAdmin):
    inlines = [RetailerProfileInline]
   

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Retailer)