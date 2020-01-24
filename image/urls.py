from django.urls import path, include
from rest_framework.routers import DefaultRouter
from image import views


router = DefaultRouter()
# router.register(r'image/<str:ward>', views.ImageViewSet)
router.register(r'deleted', views.DeletedImageViewSet)

# The API URLs are now determined automatically by the router.

urlpatterns = [
    path('count', views.TestViewSet.as_view()),
    path('image/<str:ward>', views.ImageViewSet.as_view({'get':'list'}),name='image'),
    path('',include(router.urls)),
]