from rest_framework import generics
from rest_framework import permissions
from .models import Stat
from .serializer import StatSerializer


# Create your views here.


class StatListView(generics.ListCreateAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly, }
