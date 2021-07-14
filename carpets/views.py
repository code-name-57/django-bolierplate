from django.db.models import query
from django.forms import widgets, CheckboxSelectMultiple
from django.http import HttpResponse
from django.shortcuts import render
import django_filters
from .models import Carpet, Design, Collection
from .forms import CarpetImageForm, BrandForm

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
    return render(request, "carpets_index.html", context)


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
