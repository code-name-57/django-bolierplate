"""
These are the main website uls and also handles the API
call used in the display of the website.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from rest_framework import routers

from .viewsets import *
from . import views

router = routers.DefaultRouter()
router.register(r'Brands', BrandViewSet)
router.register(r'Collections', CollectionViewSet)
router.register(r'Designs', DesignViewSet)
router.register(r'Carpets', CarpetViewSet)
router.register(r'Sizes', SizeViewSet)
router.register(r'Colors', ColorViewSet)

urlpatterns = [
    path('about', TemplateView.as_view(template_name='cube/company/about.html'), name='about'),
    path('',  views.showAllCarpets, name='list'),

    path('list', views.showAllCarpets, name='list'),

    path('collection/<int:collection_id>', views.collectionList, name='collection'),
    path('size/<int:size_id>', views.sizeList, name='size'),

    path('design_list', views.showAllDesigns, name = 'list2'),
    path('details/<int:carpet_id>', views.carpet_detail_view, name='carpets'),
    path('rest/', include(router.urls)),

]