from django.shortcuts import render
from rest_framework import viewsets
from image.serializers import ImageSerializer, DeletedImageSerializer
from image.models import ImageData, DeletedImage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = ImageData.objects.all()
    permission_classes = []

    def get_queryset(self):
        # queryset = ImageData.objects.filter(Q(ward=self.kwargs['ward']) | Q(ward='0'))
        queryset = ImageData.objects.filter(Q(ward=self.kwargs['ward']))
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        id = instance.id
        delted_image = DeletedImage.objects.create(image_id=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeletedImageViewSet(viewsets.ModelViewSet):
    serializer_class = DeletedImageSerializer
    queryset = DeletedImage.objects.all()
    permission_classes = []


class TestViewSet(APIView):

    def get(self, request):
        c = ImageData.objects.all().count()

        return Response({'count': c})
