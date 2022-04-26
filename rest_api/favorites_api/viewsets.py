from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import IsAuthenticated

class FavoriteListViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = FavoriteListSerializer

    def get_queryset(self):
        return FavoriteList.objects.filter(store_user=self.request.user).all()

class FavoriteItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer

class SceneImageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = SceneImage.objects.all()
    serializer_class = SceneImageSerializer
