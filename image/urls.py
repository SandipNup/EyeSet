from django.urls import path, include
from rest_framework.routers import DefaultRouter
from image import views


router = DefaultRouter()
router.register(r'image', views.ImageViewSet)

# The API URLs are now determined automatically by the router.

urlpatterns = [
    path('',include(router.urls))
]