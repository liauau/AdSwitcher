from django.shortcuts import render
from django.views import generic
from switcher.models.ad_config import AppNode
from switcher.forms import PkgNameForm
from django.http import HttpResponseRedirect


class IndexView(generic.ListView):
    queryset = AppNode.objects.all()
    template_name = 'index.html'
    context_object_name = 'node_set'


class DetailView(generic.DetailView):
    model = AppNode
    template_name = 'detail.html'
    context_object_name = 'node'


def get_pkg(request):
    if request.method == 'POST':
        form = PkgNameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = PkgNameForm()

    return render(request, 'name.html', {'form': form})
