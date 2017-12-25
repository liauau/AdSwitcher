from django.conf.urls import url
from switcher.views import api, site

urlpatterns = [
    url(r'^$', site.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9a-zA-Z.]+)$', site.DetailView.as_view(), name='detail'),
    url(r'^v1/ad_config/?$', api.AdConfigListView.as_view(), name='api_ad_config_list'),
    url(r'^v1/ad_config/get/?$', api.AdConfigDetailView.as_view(), name='api_ad_config_detail'),
    url(r'^v1/family/?$', api.AppFamilyListView.as_view(), name='api_app_family_list'),
    url(r'^v1/family/get/?$', api.AppFamilyDetailView.as_view(), name='api_app_family_detail'),
    url(r'^v1/ad_crack/?$', api.AdContextListView.as_view(), name='api_ad_crack_list'),
    url(r'^v1/ad_crack/get/?$', api.AdContextDetailView.as_view(), name='api_ad_crack_detail'),
    url(r'^v1/jh_ck/?$', api.JhCrackListView.as_view(), name='api_jh_crack_list'),
    url(r'^v1/jh_ck/get/?$', api.JhCrackDetailView.as_view(), name='api_jh_crack_detail'),
    url(r'^v1/ad_sdk/?$', api.SdkView.as_view(), name='ad_sdk'),
    url(r'^ip/?$', api.get_ip, name='ad_ip'),
]
