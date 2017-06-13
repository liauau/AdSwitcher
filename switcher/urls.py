from django.conf.urls import url
from switcher import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9a-zA-Z.]+)$', views.DetailView.as_view(), name='detail'),
    url(r'^v1/get_ad_config_list/$', views.ApiGetAdConfigListView.as_view(), name='api_ad_config_list'),
    url(r'^v1/get_ad_config/$', views.ApiGetAdConfigDetailView.as_view(), name='api_ad_config_detail'),
]
