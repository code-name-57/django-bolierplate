from django.db.models import query
from django.forms import widgets, CheckboxSelectMultiple
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
import django_filters
from .models import Carpet, Design, Collection, DesignInColor, Color, Size
from django.views.generic import DetailView
from django.core.paginator import Paginator
# from catalog import models

class CarpetPropertyFilter(django_filters.FilterSet):
    designColor__color = django_filters.ModelMultipleChoiceFilter(label='Colors', queryset=Color.objects.all(), widget=CheckboxSelectMultiple)
    designColor__design__collection = django_filters.ModelMultipleChoiceFilter(label='Collections', queryset=Collection.objects.all(), widget=CheckboxSelectMultiple)
    size = django_filters.ModelMultipleChoiceFilter(label='Sizes', queryset=Size.objects.all(), widget=CheckboxSelectMultiple)
    class Meta:
        model = Carpet
        fields = {'designColor__color', 'designColor__design__collection'}

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "cube/shop/sign-in.html")

def signup(request):
    return render(request, "cube/shop/register.html")

def showAllCarpets(request):
    available_carpets = Carpet.objects.all()
    carpet_filter = CarpetPropertyFilter(request.GET, queryset=available_carpets)
    paginator = Paginator(carpet_filter.qs, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj" : page_obj, "form" : carpet_filter.form}
    return render(request, "cube/shop/shop-listing-sidebar.html", context)

class DesignInColorPropertyFilter(django_filters.FilterSet):
    color = django_filters.ModelMultipleChoiceFilter(label='Colors', field_name='color', queryset=Color.objects.all(), widget=CheckboxSelectMultiple)
    design__collection__name = django_filters.ModelMultipleChoiceFilter(label='Collections', field_name='design__collection__name', queryset=Collection.objects.all(), widget=CheckboxSelectMultiple)
    class Meta:
        model = DesignInColor
        fields = {'color', 'design__collection__name'}

def showAllDesigns(request):
    available_Designs = DesignInColor.objects.all()
    design_filter = DesignInColorPropertyFilter(request.GET, queryset=available_Designs)
    context = {"filter": design_filter}
    return render(request, "cube/shop/shop-listing.html", context)

def carpet_detail_view(request, carpet_id):
    carpet = get_object_or_404(Carpet, id=carpet_id)
    otherSizes = Carpet.objects.filter(designColor = carpet.designColor)
    otherColors = DesignInColor.objects.filter(design=carpet.designColor.design)
    otherDesigns = DesignInColor.objects.filter(color=carpet.designColor.color, design__collection=carpet.designColor.design.collection)
    return render(request, "cube/shop/shop-product.html", {"carpet": carpet, "otherSizes": otherSizes, "otherColors": otherColors, "otherDesigns": otherDesigns})

def collectionList(request, collection_id):
    designColors = DesignInColor.objects.filter(design__collection__id=collection_id)
    paginator = Paginator(designColors, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj" : page_obj}
    return render(request, "cube/shop/shop-listing.html", context)

def sizeList(request, size_id):
    available_carpets = Carpet.objects.filter(size__id = size_id)
    carpet_filter = CarpetPropertyFilter(request.GET, queryset=available_carpets)
    paginator = Paginator(carpet_filter.qs, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj" : page_obj, "form" : carpet_filter.form}
    return render(request, "cube/shop/shop-listing-sidebar.html", context)

