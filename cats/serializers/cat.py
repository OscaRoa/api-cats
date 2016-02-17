from rest_framework import serializers
from cats.models import Cat, Breed
from django.contrib.auth.models import User


class CatSerializer(serializers.ModelSerializer):
    """Cat Serializer Class"""

    owner = serializers.SlugRelatedField(
        read_only=False,
        queryset=User.objects.all(),
        slug_field='username'
    )

    breed = serializers.SlugRelatedField(
        read_only=False,
        queryset=Breed.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Cat
        fields = ('id', 'name', 'breed', 'age', 'photo', 'owner')
