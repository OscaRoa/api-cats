from django.conf.urls import url
from .views import (
    UserList,
    UserDetail
)

urlpatterns = [
    # User URL's
    url(r'^users/$', UserList.as_view(), name='list'),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view(), name='detail'),
]
