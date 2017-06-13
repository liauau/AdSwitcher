from rest_framework import generics
from rest_framework import permissions
from switcher.models.ad_config import AppNode
from switcher.serializer.ad_config import AppNodeSerializer
from switcher.models.app_family import Member
from switcher.serializer.app_family import MemberSerializer
from django.shortcuts import get_object_or_404


class AdConfigListView(generics.ListCreateAPIView):
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


class AdConfigDetailView(generics.RetrieveUpdateDestroyAPIView):
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


class AppFamilyListView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def filter_queryset(self, queryset):
        pkg_name = self.request.query_params.get('_appPkgName')
        if pkg_name:
            queryset = queryset.exclude(pkg_name=pkg_name)
        return super().filter_queryset(queryset)


class AppFamilyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self):
        query_params = self.request.query_params
        pkg_name = query_params.get('_appPkgName')
        filter_kwargs = {self.lookup_field: pkg_name}

        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
