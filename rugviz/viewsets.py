from rest_framework import viewsets
from .serializers import *

class EnvColorViewset(viewsets.ModelViewSet):
    queryset = EnvColor.objects.all()
    serializer_class = EnvColorSerializer

class FloorTypeViewset(viewsets.ModelViewSet):
    queryset = FloorType.objects.all()
    serializer_class = FloorTypeSerializer

class FloorTextureViewset(viewsets.ModelViewSet):
    queryset = FloorTexture.objects.all()
    serializer_class = FloorTextureSerializer