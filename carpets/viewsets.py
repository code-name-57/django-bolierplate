from rest_framework import viewsets
from .serializers import *

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class DesignViewSet(viewsets.ModelViewSet):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer

class CarpetViewSet(viewsets.ModelViewSet):
    queryset = Carpet.objects.all()
    serializer_class = CarpetSerializer
    