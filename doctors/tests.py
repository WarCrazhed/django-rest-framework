from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from patients.models import Patient
from doctors.models import Doctor

# Create your tests here.
class ViewSetTests(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            first_name='John',
            last_name='Doe',
            date_of_birth='1990-01-01',
            contact_number='1234567890',
            email='john.doe@example.com',
            address='123 Main St, Anytown, USA',
            medical_history='No known allergies. Previous surgery in 2015.'
        )
        self.doctor = Doctor.objects.create(
            first_name='Jane',
            last_name='Smith',
            qualification='Profesional',
            contact_number='0987654321',
            email='jane.smith@example.com',
            address='456 Oak Ave, Somewhere, USA',
            biography='Dr. Jane Smith is a board-certified physician with over 10 years of experience in internal medicine. She is dedicated to providing comprehensive care to her patients and has a special interest in preventive medicine and chronic disease management.',
            is_on_vacation=False
        )
        self.client = APIClient()

    def test_list_should_return_200(self):
        url = reverse(
            'doctor-appointments', kwargs={'pk': self.doctor.id}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)