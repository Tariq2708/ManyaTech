from rest_framework import serializers
from .models import Frame

class FrameSerializer(serializers.ModelSerializer):
    # Serializer class for the Frame model

    class Meta:
        # Meta class to specify model and fields to be included in the serialization
        model = Frame
        fields = '__all__'  # Include all fields from the Frame model
