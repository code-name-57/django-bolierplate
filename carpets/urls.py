from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-new', views.showimage),
    path('list', views.showAllCarpets, name='list'),
    path('product/<design_id>/<color_id>/<size_id>', views.CarpetDetailView.as_view(), name='details'),
    path('details/<int:design_id>/<int:color_id>/<int:size_id>', views.carpet_detail_view, name='carpets'),
    path('design/<pk>', views.DesignDetailView.as_view(), name="design"),
]