from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import DoctorSerializer
from .models import Doctor
from .permissions import IsDoctor
from bookings.serializers import AppointmentSerializer
from rest_framework.permissions import IsAuthenticated

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticated, IsDoctor]

    @action(['POST'], detail=True, url_path='set-on-vacation')
    def set_on_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({'status': 'Doctor is on vacation'})
        
    @action(['POST'], detail=True, url_path='set-off-vacation')
    def set_off_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({'status': 'Doctor is not on vacation'})

    @action(['POST', 'GET'], detail=True, serializer_class=AppointmentSerializer)
    def appointments(self, request, pk):
        doctor = self.get_object()

        if request.method == 'POST':
            data = request.data.copy()
            data['doctor'] = doctor.id
            serializer = AppointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        if request.method == 'GET':
            appointments = doctor.appointments.all()
            # Otra forma:
            # appointments = Appointment.objects.filter(doctor=doctor)
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)