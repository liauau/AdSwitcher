from django.conf.urls import url
from .views import StatListView

urlpatterns = [
    url(r'^v1/stat/?$', StatListView.as_view(), name='stat_list'),
]
