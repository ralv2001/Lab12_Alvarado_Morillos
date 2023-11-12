from rest_framework import serializers

from rest_api.models import Equipo, Liga


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'


class LigaSerializer(serializers.HyperlinkedModelSerializer):
    equipo = EquipoSerializer(read_only=True)

    class Meta:
        model = Liga
        fields = '__all__'
