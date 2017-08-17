from rest_framework import generics
from rest_framework import permissions

from .models import Stat
from .serializer import StatSerializer


class StatListView(generics.CreateAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly, }
