from django.shortcuts import render
from django.views import generic
from switcher.models.ad_config import AppNode
from switcher.forms import RoleForm
from django.http import HttpResponseRedirect
from switcher.models.user import User


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
        param_dict = request.POST
        current_pkg_name = request.POST['input_pkg_name']
    else:
        param_dict = {}

    # return render(request, 'name.html', {'form': form, 'param_dict': param_dict})
    return render(request, 'name.html', {
        'param_dict': param_dict,
        'current_pkg_name': current_pkg_name
    })


def login(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            password = data.get('password')
            member = User.objects.get(name=name)

            if member and member.password == password:
                return render(request, 'welcome.html', {
                    'user': data.get('name')
                })
    else:
        form = RoleForm()

    return render(request, 'login.html', {
        'form': form
    })


def register(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            password = data.get('password')
            member = User(name=name, password=password)
            member.save()
            return render(request, 'login.html', {'form': form})
    else:
        form = RoleForm()

    return render(request, 'register.html', {
        'form': form
    })
