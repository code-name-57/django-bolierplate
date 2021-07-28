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
    
class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class EnvColorViewset(viewsets.ModelViewSet):
    queryset = EnvColor.objects.all()
    serializer_class = EnvColorSerializer

class FloorTypeViewset(viewsets.ModelViewSet):
    queryset = FloorType.objects.all()
    serializer_class = FloorTypeSerializer

class FloorTextureViewset(viewsets.ModelViewSet):
    queryset = FloorTexture.objects.all()
    serializer_class = FloorTextureSerializer