"""
These are the main website uls and also handles the API
call used in the display of the website.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from rest_framework import routers



urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='cube/account/sign-in.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='list'), name='logout'),

    path('register', TemplateView.as_view(template_name='cube/account/register.html'), name='register'),
    path('billing', TemplateView.as_view(template_name='cube/account/account-billing.html'), name='billing'),
    path('orders', TemplateView.as_view(template_name='cube/account/account-orders.html'), name='orders'),
    path('settings', TemplateView.as_view(template_name='cube/account/account-settings.html'), name='settings'),
    path('account', TemplateView.as_view(template_name='cube/account/account.html'), name='account'),
    path('forgot', TemplateView.as_view(template_name='cube/account/forgot-password.html'), name='forgot'),
    path('cart', TemplateView.as_view(template_name='cube/shop/shop-cart.html'), name='cart'),

]