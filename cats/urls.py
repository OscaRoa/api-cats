from django.conf.urls import url
from cats.views.cat import (
    CatList,
    CatDetail
)
from cats.views.breed import (
    BreedList,
    BreedDetail
)

urlpatterns = [
    # Cats URL's
    url(r'^cats/$', CatList.as_view(), name='list'),
    url(r'^cats/(?P<pk>\d+)/$', CatDetail.as_view(), name='detail'),
    # Breeds URL's
    url(r'^breeds/$', BreedList.as_view(), name='list_breeds'),
    url(r'^breeds/(?P<pk>\d+)/$', BreedDetail.as_view(), name='detail_breed'),
]
