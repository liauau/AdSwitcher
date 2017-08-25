from django.shortcuts import render
from django.views import generic
from rest_framework import generics
from rest_framework import permissions

from .models import Stat, Event, EventInfo
from .serializer import StatSerializer


class StatListView(generics.ListCreateAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly, }


class StatDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly, }


class StatShowView(generic.ListView):
    queryset = Stat.objects.all()
    template_name = 'statistics/index.html'
    context_object_name = 'node_set'


def count(request):
    record_count = Stat.objects.all().count()
    user_ids = Stat.objects.distinct('user_id').count()
    events = [e for e in Event.objects.distinct('name')]
    # event_dict = dict()
    event_info_list = []
    for e in events:
        # c = Event.objects.filter(name=e.name).count()
        # event_dict[e.name] = c
        einfo = EventInfo()
        einfo.name = e.name
        einfo.count = Event.objects.filter(name=e.name).count()
        # einfo.user_count = [e.__dict__ for e in Event.objects.select_related()]
        einfo.user_count = Stat.objects.filter(events__name=e.name).distinct('user_id').count()

        event_info_list.append(einfo)

    for e in event_info_list:
        print(e.name + ' ' + str(e.count))

    context = {
        'record_count': record_count,
        'user_ids': user_ids,
        'event_info_list': event_info_list,
    }
    return render(request, 'statistics/index_stat.html', context)


def day_active_user(request):
    pass


def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    # template = loader.get_template('statistics/' + load_template)
    template = 'statistics/' + load_template
    return render(request, template, context)
