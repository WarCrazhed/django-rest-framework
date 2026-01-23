from rest_framework import serializers
from .models import Appointment, MedicalNote
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer, MedicalNoteSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)
    medical_notes = MedicalNoteSerializer(many=True, read_only=True)

    class Meta:
        model = Appointment
        fields = "__all__"

class MedicalNoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = "__all__"