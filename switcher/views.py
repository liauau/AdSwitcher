from django.views import generic
from rest_framework import generics
from rest_framework import permissions
from .models.config import AppNode
from .serializer import AppNodeSerializer
from django.shortcuts import get_object_or_404


# Create your views here.

class IndexView(generic.ListView):
    queryset = AppNode.objects.all()
    template_name = 'index.html'
    context_object_name = 'node_set'


class DetailView(generic.DetailView):
    model = AppNode
    template_name = 'detail.html'
    context_object_name = 'node'


class ApiGetAdConfigListView(generics.ListCreateAPIView):
    queryset = AppNode.objects.all()
    serializer_class = AppNodeSerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly, }

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def filter_queryset(self, queryset):
        query_params = self.request.query_params
        pkg_name = query_params.get('_appPkgName')
        if pkg_name:
            queryset = queryset.filter(pkg_name=pkg_name)
        return super().filter_queryset(queryset)


class ApiGetAdConfigDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppNode.objects.all()
    serializer_class = AppNodeSerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly, }

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_object(self):
        query_params = self.request.query_params
        pkg_name = query_params.get('_appPkgName')
        filter_kwargs = {self.lookup_field: pkg_name}

        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
