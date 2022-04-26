"""
This is for handling API calls b/w unity and database.
"""
from django.urls import path, include

from rest_framework import routers

from .rugviz_api.viewsets import *
from .catalog_api.viewsets import *
from .favorites_api.viewsets import *

router = routers.DefaultRouter()

router.register(r'EnvColors', EnvColorViewset)
router.register(r'FloorTypes', FloorTypeViewset)
router.register(r'FloorTextures', FloorTextureViewset)
router.register(r'CarpetPhoto', CarpetPictureViewset)

router.register(r'Brands', BrandViewSet)
router.register(r'Collections', CollectionViewSet)
router.register(r'Designs', DesignViewSet)
router.register(r'Carpets', CarpetViewSet)
router.register(r'Sizes', SizeViewSet)
router.register(r'Colors', ColorViewSet)

router.register(r'FavoriteList', FavoriteListViewSet, basename='FavoriteList')
router.register(r'FavoriteItem', FavoriteItemViewSet)
router.register(r'SceneImage', SceneImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
