from django.shortcuts import render
from rest_framework import viewsets
from image.serializers import ImageSerializer
from image.models import ImageData

# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = ImageData.objects.all()
    permission_classes = []

