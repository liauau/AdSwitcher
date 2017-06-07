from django.conf.urls import url, include
from .views import StatListView

urlpatterns = [
    url(r'^stat', StatListView.as_view(), name='stat_list'),
]
