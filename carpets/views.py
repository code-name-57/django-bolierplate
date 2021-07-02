from django.http import HttpResponse
from django.shortcuts import render
from .models import Carpet
from .forms import CarpetImageForm, BrandForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


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
