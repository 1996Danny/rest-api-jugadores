from .models import Jugadores
from rest_framework import serializers


class JugadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugadores
        # fields = ['id', 'nombre','edad', 'imagen', 'descripcion']
        fields = "__all__"
