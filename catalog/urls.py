from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from carpets.viewsets import *

router = routers.DefaultRouter()
router.register(r'Brands', BrandViewSet)
router.register(r'Collections', CollectionViewSet)
router.register(r'Designs', DesignViewSet)
router.register(r'Carpets', CarpetViewSet)
router.register(r'Sizes', SizeViewSet)
router.register(r'Colors', ColorViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    # path('add-new', views.showimage),
    # path('list', views.showAllCarpets, name='list'),
    # path('product/<design_id>/<color_id>/<size_id>', views.CarpetDetailView.as_view(), name='details'),
    # path('details/<int:design_id>/<int:color_id>/<int:size_id>', views.carpet_detail_view, name='carpets'),
    # path('design/<pk>', views.DesignDetailView.as_view(), name="design"),
    path('rest/', include(router.urls)),

]