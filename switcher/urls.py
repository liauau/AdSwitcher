from django.conf.urls import url
from switcher.views import api, site

urlpatterns = [
    url(r'^$', site.IndexView.as_view(), name='index'),
    url(r'^pkg_name/$', site.get_pkg, name='pkg'),
    url(r'^login/$', site.login, name='login'),
    url(r'^register/$', site.register, name='register'),
    url(r'^(?P<pk>[0-9a-zA-Z.]+)$', site.DetailView.as_view(), name='detail'),
    url(r'^v1/ad_config/$', api.AdConfigListView.as_view(), name='api_ad_config_list'),
    url(r'^v1/ad_config/get/$', api.AdConfigDetailView.as_view(), name='api_ad_config_detail'),
    url(r'^v1/family/$', api.AppFamilyListView.as_view(), name='api_app_family_list'),
    url(r'^v1/family/get/$', api.AppFamilyDetailView.as_view(), name='api_app_family_detail'),
]
