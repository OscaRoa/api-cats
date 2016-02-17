from cats.models import Cat
from rest_framework import generics, permissions, filters
from cats.serializers.cat import CatSerializer


class CatList(generics.ListCreateAPIView):
    """Cat List API View"""
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    # Search in endpoint
    filter_backends = (filters.SearchFilter,)
    search_fields = ('$breed__name', '$name',
                     '$owner__username')

    def get_queryset(self):
        queryset = Cat.objects.all()
        name = self.request.query_params.get('name', None)
        breed = self.request.query_params.get('breed', None)
        owner = self.request.query_params.get('owner', None)

        if name is not None:
            queryset = queryset.filter(name=name)

        if breed is not None:
            queryset = queryset.filter(breed=breed)

        if owner is not None:
            queryset = queryset.filter(owner=owner)

        return queryset


class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    """Cat detail API View"""
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
