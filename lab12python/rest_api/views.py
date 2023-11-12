from rest_framework import viewsets

from rest_api.models import Liga, Equipo
from rest_api.serializers import LigaSerializer, EquipoSerializer


class EquipoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

    def get_queryset(self):
        return self.queryset.all()


class LigaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Liga.objects.select_related('equipo').all().order_by('puntos')
    serializer_class = LigaSerializer

