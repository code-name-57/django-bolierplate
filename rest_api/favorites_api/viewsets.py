from rest_framework import viewsets
from .serializers import *
# from rest_framework.permissions import IsAuthenticated

class FavoriteListViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = FavoriteList.objects.filter()
    serializer_class = FavoriteListSerializer

class FavoriteItemViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer

class SceneImageViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = SceneImage.objects.all()
    serializer_class = SceneImageSerializer
