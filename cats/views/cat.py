from cats.models import Cat
from rest_framework import generics, permissions
from cats.serializers.cat import CatSerializer


class CatList(generics.ListCreateAPIView):
    """Cat List API View"""
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    """Cat detail API View"""
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
