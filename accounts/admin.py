from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

from .models import Address, OrderItem, Retailer, Consumer, Order, Address
# Register your models here.


class RetailerProfileInline(admin.StackedInline):
    model = Retailer

class ConsumerProfileInline(admin.StackedInline):
    model = Consumer

class CustomUserAdmin(UserAdmin):
    inlines = [RetailerProfileInline, ConsumerProfileInline]
   
class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem
    show_change_link = False

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTabularInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Retailer)
admin.site.register(Consumer)
admin.site.register(Order, OrderAdmin)
admin.site.register(Address)
