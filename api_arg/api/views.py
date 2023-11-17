from .models import Jugadores
from .serializers import JugadoresSerializer
from rest_framework import viewsets

# Create your views here.


class JugadoresViewSet(viewsets.ModelViewSet):
    queryset = Jugadores.objects.all()  # SELECT * FROM Jugadores
    serializer_class = JugadoresSerializer
