from rest_framework import serializers
from .models import Doctor, Department, DoctorAvailability, MedicalNote

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

    def validate_email(self, value):
        # value = "hola@example.com"
        if "@example.com" in value:
            return value
        raise serializers.ValidationError("Email must be from the domain example.com")
    
    def validate(self, attrs):
        if len(attrs['contact_number']) < 10 and attrs['is_on_vacation'] == True:
            raise serializers.ValidationError("Contact number must be 10 digits when doctor is on vacation")
        return super().validate(attrs)

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = "__all__"

class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = "__all__"