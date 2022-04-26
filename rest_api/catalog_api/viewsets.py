from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import IsAuthenticated  # <-- Here

class BrandViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CollectionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class DesignViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Design.objects.all()
    serializer_class = DesignSerializer

class CarpetViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Carpet.objects.all()
    serializer_class = CarpetSerializer
    
class SizeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class ColorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
