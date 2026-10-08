from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import User
from patients.models import Patient
from doctors.models import Doctor
from .models import PatientDoctorMapping


class MappingTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="mappinguser@example.com",
            name="Mapping User",
            password="TestPassword123!",
        )

        self.other_user = User.objects.create_user(
            email="otheruser@example.com",
            name="Other User",
            password="TestPassword123!",
        )

        self.client.force_authenticate(user=self.user)

        self.patient = Patient.objects.create(
            created_by=self.user,
            name="Alice Smith",
        )

        self.other_patient = Patient.objects.create(
            created_by=self.other_user,
            name="Other Patient",
        )

        self.doctor = Doctor.objects.create(
            name="Dr. Sarah Wilson",
            specialization="Cardiology",
        )

        self.mapping_url = reverse("mapping-list-create")

    def test_create_mapping(self):
        response = self.client.post(
            self.mapping_url,
            {
                "patient": self.patient.id,
                "doctor": self.doctor.id,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertTrue(
            PatientDoctorMapping.objects.filter(
                patient=self.patient,
                doctor=self.doctor,
            ).exists()
        )

    def test_duplicate_mapping_fails(self):
        PatientDoctorMapping.objects.create(
            patient=self.patient,
            doctor=self.doctor,
        )

        response = self.client.post(
            self.mapping_url,
            {
                "patient": self.patient.id,
                "doctor": self.doctor.id,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    def test_cannot_assign_doctor_to_other_users_patient(self):
        response = self.client.post(
            self.mapping_url,
            {
                "patient": self.other_patient.id,
                "doctor": self.doctor.id,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    def test_delete_mapping(self):
        mapping = PatientDoctorMapping.objects.create(
            patient=self.patient,
            doctor=self.doctor,
        )

        url = reverse(
            "mapping-delete",
            kwargs={"pk": mapping.id},
        )

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )

        self.assertFalse(
            PatientDoctorMapping.objects.filter(
                id=mapping.id
            ).exists()
        )