from django.views import generic
from switcher.models.ad_config import AppNode


class IndexView(generic.ListView):
    queryset = AppNode.objects.all()
    template_name = 'index.html'
    context_object_name = 'node_set'


class DetailView(generic.DetailView):
    model = AppNode
    template_name = 'detail.html'
    context_object_name = 'node'
