from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions

from switcher.models.ad_config import AppNode
from switcher.models.ad_crack import CrackNode
from switcher.models.app_family import Member
from switcher.models.jh_crack import JhNode
from switcher.serializer.ad_config import AppNodeSerializer
from switcher.serializer.ad_crack import CrackNodeSerializer
from switcher.serializer.app_family import MemberSerializer
from switcher.serializer.jh_crack import JhNodeSerializer


def get_queryset(self, queryset):
    query_params = self.request.query_params
    pkg_name = query_params.get('_appPkgName')
    if pkg_name:
        queryset = queryset.filter(pkg_name=pkg_name)
    return queryset


def get_object(self):
    query_params = self.request.query_params
    pkg_name = query_params.get('_appPkgName')
    filter_kwargs = {self.lookup_field: pkg_name}

    queryset = self.filter_queryset(self.get_queryset())
    obj = get_object_or_404(queryset, **filter_kwargs)

    # May raise a permission denied
    self.check_object_permissions(self.request, obj)
    return obj


class AdConfigListView(generics.ListCreateAPIView):
    queryset = AppNode.objects.all()
    serializer_class = AppNodeSerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly, }

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def filter_queryset(self, queryset):
        queryset = get_queryset(self, queryset)
        return super().filter_queryset(queryset)


class AdConfigDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppNode.objects.all()
    serializer_class = AppNodeSerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly, }

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_object(self):
        return get_object(self)


class AppFamilyListView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def filter_queryset(self, queryset):
        query_params = self.request.query_params
        pkg_name = query_params.get('_appPkgName')
        if pkg_name:
            queryset = queryset.filter(Q(public=True) | Q(pkg_name=pkg_name))
        return super().filter_queryset(queryset)


class AppFamilyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self):
        return get_object(self)


class AdContextListView(generics.ListCreateAPIView):
    queryset = CrackNode.objects.all()
    serializer_class = CrackNodeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AdContextDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CrackNode.objects.all()
    serializer_class = CrackNodeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self):
        self.lookup_field = 'pk'
        return get_object(self)


class JhCrackListView(generics.ListCreateAPIView):
    queryset = JhNode.objects.all()
    serializer_class = JhNodeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class JhCrackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JhNode.objects.all()
    serializer_class = JhNodeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self):
        self.lookup_field = 'pk'
        return get_object(self)
