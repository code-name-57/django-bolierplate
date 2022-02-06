"""
This is for handling API calls b/w unity and database.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from .viewsets import *

router = routers.DefaultRouter()

router.register(r'EnvColors', EnvColorViewset)
router.register(r'FloorTypes', FloorTypeViewset)
router.register(r'FloorTextures', FloorTextureViewset)
router.register(r'CarpetPhoto', CarpetPictureViewset)

urlpatterns = [
    path('rest/', include(router.urls)),
]
