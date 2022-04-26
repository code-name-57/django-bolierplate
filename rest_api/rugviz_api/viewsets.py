from rest_framework import viewsets
from .serializers import *
from rugviz.models import *

class EnvColorViewset(viewsets.ModelViewSet):
    queryset = EnvColor.objects.all()
    serializer_class = EnvColorSerializer

class FloorTypeViewset(viewsets.ModelViewSet):
    queryset = FloorType.objects.all()
    serializer_class = FloorTypeSerializer

class FloorTextureViewset(viewsets.ModelViewSet):
    queryset = FloorTexture.objects.all()
    serializer_class = FloorTextureSerializer

class CarpetPictureViewset(viewsets.ModelViewSet):
    queryset = CarpetPicture.objects.all()
    serializer_class = CarpetPictureSerializer