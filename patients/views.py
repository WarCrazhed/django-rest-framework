from .serializers import PatientSerializer
from .models import Patient
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView


# GET /api/patients/ => Listar
# POST /api/patients/ => Crear
# GET /api/patients/<pk> => Detalle
# PUT /api/patients/<pk> => Modificar
# DELETE /api/patients/<pk> => Eliminar

class ListPatientsView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class DetailPatientView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()