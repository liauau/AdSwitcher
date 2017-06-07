from django.conf.urls import url, include
from switcher import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9a-zA-Z.]+)$', views.DetailView.as_view(), name='detail'),
    url(r'^v1/api/(?P<pk>[0-9a-zA-Z.-_]+)/$', views.ApiDetailView.as_view(), name='api_detail'),
    url(r'^v1/api/$', views.ApiListView.as_view(), name='api_list'),
]
