from rest_framework import viewsets
from .models import Frame
from .serializers import FrameSerializer

# ViewSet for handling Frame model CRUD operations
class FrameViewSet(viewsets.ModelViewSet):
    # Define the queryset to retrieve all Frame instances from the database
    queryset = Frame.objects.all()
    # Specify the serializer class to be used for serializing/deserializing Frame instances
    serializer_class = FrameSerializer
