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

from rest_framework.authtoken.views import obtain_auth_token

from .views import SignUpView, checkout, register_as_consumer, register_as_retailer, add_to_cart, deduct_from_cart, remove_from_cart


urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='cube/account/sign-in.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='list'), name='logout'),
    
    path('forgot', auth_views.PasswordResetView.as_view(template_name='cube/account/password-reset/forgot-password.html', html_email_template_name='cube/account/password-reset/password-reset-email.html', subject_template_name='cube/account/password-reset/password-reset-subject.txt'), name='forgot'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='cube/account/password-reset/forgot-password-done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='cube/account/password-reset/forgot-password-confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='cube/account/password-reset/forgot-password-complete.html'), name='password_reset_complete'),
    path('register_retailer', register_as_retailer, name="register_retailer"),
    path('register_consumer', register_as_consumer, name="register_consumer"),

    # path('signup', SignUpView.as_view(), name='signup' ),
    
    path('register', SignUpView.as_view(), name='register'),
    path('billing', TemplateView.as_view(template_name='cube/account/account-billing.html'), name='billing'),
    path('orders', TemplateView.as_view(template_name='cube/account/account-orders.html'), name='orders'),
    path('settings', TemplateView.as_view(template_name='cube/account/account-settings.html'), name='settings'),
    path('account', TemplateView.as_view(template_name='cube/account/account.html'), name='account'),
    # path('forgot', TemplateView.as_view(template_name='cube/account/forgot-password.html'), name='forgot'),
    path('cart', TemplateView.as_view(template_name='cube/account/shop-cart.html'), name='cart'),
    path('api-token-auth', obtain_auth_token, name='api_token_auth'),

    path('add_to_cart/<int:carpet_id>/<int:redirect_to_cart>', add_to_cart, name='add_to_cart'),
    path('add_to_cart/<int:carpet_id>', add_to_cart, name='add_to_cart'),
    path('deduct_from_cart/<int:carpet_id>', deduct_from_cart, name='deduct_from_cart'),
    path('remove_from_cart/<int:carpet_id>', remove_from_cart, name='remove_from_cart'),
    path('checkout', checkout, name='checkout'),
]