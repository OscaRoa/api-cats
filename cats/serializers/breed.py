from rest_framework import serializers
from cats.models import Breed


class BreedSerializer(serializers.ModelSerializer):
    """Breed Serializer Class"""

    class Meta:
        model = Breed
        fields = ('id', 'name',)
