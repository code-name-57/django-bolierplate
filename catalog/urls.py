"""
These are the main website uls and also handles the API
call used in the display of the website.
"""

from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('about', TemplateView.as_view(template_name='cube/company/about.html'), name='about'),
    path('',  views.showAllCarpets, name='list'),

    path('list', views.showAllCarpets, name='list'),

    path('collection/<int:collection_id>', views.collectionList, name='collection'),
    path('size/<int:size_id>', views.sizeList, name='size'),

    path('design_list', views.showAllDesigns, name = 'list2'),
    path('details/<int:carpet_id>', views.carpet_detail_view, name='carpets'),
    path('design/<int:design_id>', views.design_detail_view, name='design'),
]
