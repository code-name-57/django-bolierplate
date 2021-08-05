from django.db.models import query
from django.forms import widgets, CheckboxSelectMultiple
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
import django_filters
from .models import Carpet, Design, Collection
from .forms import CarpetImageForm, BrandForm
from django.views.generic import DetailView

from carpets import models

class CarpetPropertyFilter(django_filters.FilterSet):
    design = django_filters.ModelMultipleChoiceFilter(queryset=Design.objects.all(), widget=CheckboxSelectMultiple)
    design__collection = django_filters.ModelMultipleChoiceFilter(queryset=Collection.objects.all(), widget=CheckboxSelectMultiple)
    class Meta:
        model = Carpet
        fields = {'design', 'design__collection'}

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def showAllCarpets(request):
    available_carpets = Carpet.objects.all()
    carpet_filter = CarpetPropertyFilter(request.GET, queryset=available_carpets)
    context = {"filter": carpet_filter}
    return render(request, "shop.html", context)


def showimage(request):

    # lastimage= Carpet.objects.last()
    # breakpoint()
    # image_file= lastimage.image_file

    form = BrandForm(request.POST or None, request.FILES or None)
    # form = CarpetImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    
    context= {
        # 'image_file': image_file,
              'form': form
              }
    
      
    return render(request, 'add_carpet.html', context)

def carpet_detail_view(request, design_id, color_id, size_id):
    carpet = get_object_or_404(Carpet, design__id=design_id, color__id=color_id, size__id=size_id)
    return render(request, "shop.html", {"carpet": carpet})
    breakpoint()
    pass
class CarpetDetailView(DetailView):
    model = Carpet
    template_name = "carpet-detail.html"

class CarpetListView(ListView):
    model = Carpet
    template_name = "carpet_list.html"

class DesignDetailView(DetailView):
    model = Design
    template_name = "design_detail.html"