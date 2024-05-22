from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FrameViewSet

# Create a router and register the FrameViewSet
router = DefaultRouter()
router.register(r'frames', FrameViewSet)

urlpatterns = [
    # Include the router-generated URLs
    path('', include(router.urls)),
]
