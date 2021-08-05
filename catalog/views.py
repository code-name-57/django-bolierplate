from django.db.models import query
from django.forms import widgets, CheckboxSelectMultiple
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
import django_filters
from .models import Carpet, Design, Collection, DesignInColor
from django.views.generic import DetailView

from carpets import models

class CarpetPropertyFilter(django_filters.FilterSet):
    designColor = django_filters.ModelMultipleChoiceFilter(queryset=DesignInColor.objects.all(), widget=CheckboxSelectMultiple)
    designColor__design__collection = django_filters.ModelMultipleChoiceFilter(queryset=Collection.objects.all(), widget=CheckboxSelectMultiple)
    class Meta:
        model = Carpet
        fields = {'designColor', 'designColor__design__collection'}

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def showAllCarpets(request):
    available_carpets = Carpet.objects.all()
    carpet_filter = CarpetPropertyFilter(request.GET, queryset=available_carpets)
    context = {"filter": carpet_filter}
    return render(request, "shop.html", context)


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