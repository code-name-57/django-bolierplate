from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Retailer, Consumer
from .forms import RetailerRegistrationForm, ConsumerRegistrationForm, UserForm


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'cube/account/register.html'

def register_as_retailer(request):
    register_user_uri = "cube/account/register_user.html"
    user = request.user
    if user.is_authenticated:
        try:
            retailer = Retailer.objects.get(user=user)
        except Retailer.DoesNotExist:
            retailer = Retailer()
        form_data_list = [request.POST] if request.POST else list()
        user_form = UserForm(*form_data_list, instance=user)
        registration_form = RetailerRegistrationForm(*form_data_list, instance = retailer)
    else:
        # Signing required
        return redirect('login')
    if request.method == "GET":
        # TODO: A user can either be a consumer or a retailer. Add that check here
        # and provide an option to switch b/w consumers and retailers.
        return render(request, register_user_uri,
                      dict(registration_form=registration_form,
                            user_form=user_form))

    if registration_form.is_valid() and user_form.is_valid():
        user_form.save()
        obj = registration_form.save(commit = False)
        obj.user = user
        obj.save()
        messages.success(request,
            "User registration request sent successfully! Verification would be complete after verification")
        # TODO: create a page to view the user profile
        return redirect('list')

    return render(request, register_user_uri,
                  dict(registration_form=registration_form,
                        user_form=user_form))


def register_as_consumer(request):
    register_user_uri = "cube/account/register_user.html"
    user = request.user
    if user.is_authenticated:
        try:
            consumer = Consumer.objects.get(user=user)
        except Consumer.DoesNotExist:
            consumer = Consumer()
        form_data_list = [request.POST] if request.POST else list()
        user_form = UserForm(*form_data_list, instance=user)
        registration_form = ConsumerRegistrationForm(*form_data_list, instance = consumer)
    else:
        # Signing required
        return redirect('login')
    if request.method == "GET":
        return render(request, register_user_uri,
                      dict(registration_form=registration_form,
                            user_form=user_form))

    if registration_form.is_valid() and user_form.is_valid():
        user_form.save()
        obj = registration_form.save(commit = False)
        obj.user = user
        obj.save()
        messages.success(request,
            "Registered as a consumer! Now you can shop online.")
        return redirect('list')

    return render(request, register_user_uri,
                  dict(registration_form=registration_form,
                        user_form=user_form))
