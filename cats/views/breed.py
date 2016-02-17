from rest_framework import generics, permissions
from cats.models import Breed
from cats.serializers.breed import BreedSerializer


class BreedList(generics.ListCreateAPIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
