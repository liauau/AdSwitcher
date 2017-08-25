from django.conf.urls import url
from statistic import views

urlpatterns = [
    url(r'^v1/stat/?$', views.StatListView.as_view(), name='stat_list'),
    url(r'^v1/stat/get/?(?P<pk>[0-9.+]+)$', views.StatDetailView.as_view(), name='stat_detail'),
    # url(r'^v1/stat/show/?$', views.StatShowView.as_view(), name='stat_show'),
    url(r'^v1/stat/show/?$', views.count, name='stat_show'),
    url(r'^.*\.html', views.gentella_html, name='gentella'),
]
