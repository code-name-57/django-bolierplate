from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Address, OrderItem, Retailer, Consumer, Order, Address, FavoriteList, FavoriteItem, SceneImage
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

class FavoriteItemInline(admin.TabularInline):
    model = FavoriteItem
    extra = 0
    show_change_link = True
    def has_add_permission(self, request, obj):
        return False

class SceneImageInline(admin.TabularInline):
    model = SceneImage

class FavoriteListAdmin(admin.ModelAdmin):
    inlines = [FavoriteItemInline]

class FavoriteItemAdmin(admin.ModelAdmin):
    inlines = [SceneImageInline]


admin.site.register(FavoriteList, FavoriteListAdmin)
admin.site.register(FavoriteItem, FavoriteItemAdmin)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Retailer)
admin.site.register(Consumer)
admin.site.register(Order, OrderAdmin)
admin.site.register(Address)
