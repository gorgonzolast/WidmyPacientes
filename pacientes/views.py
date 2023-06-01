from rest_framework import viewsets, permissions
from .models import Paciente
from .serializers import PacienteSerializer

# Create your views here.
class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PacienteSerializer