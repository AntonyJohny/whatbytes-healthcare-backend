from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import User
from doctors.models import Doctor
from patients.models import Patient
from .models import PatientDoctorMapping


class MappingAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="john@example.com",
            name="John",
            password="password123",
        )

        self.other_user = User.objects.create_user(
            email="other@example.com",
            name="Other User",
            password="password123",
        )

        self.patient = Patient.objects.create(
            created_by=self.user,
            name="John Patient",
            email="patient@example.com",
            phone="9876543210",
        )

        self.other_patient = Patient.objects.create(
            created_by=self.other_user,
            name="Other Patient",
            email="otherpatient@example.com",
            phone="9876500000",
        )

        self.doctor = Doctor.objects.create(
            name="Dr. Smith",
            specialization="Cardiology",
            email="doctor@example.com",
            phone="9876512345",
        )

        self.doctor_two = Doctor.objects.create(
            name="Dr. Jones",
            specialization="Neurology",
            email="doctor2@example.com",
            phone="9876523456",
        )

        self.client.force_authenticate(user=self.user)

    def test_create_mapping(self):
        url = reverse("mapping-list-create")

        response = self.client.post(
            url,
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

        self.assertEqual(
            PatientDoctorMapping.objects.count(),
            1,
        )

    def test_list_mappings(self):
        PatientDoctorMapping.objects.create(
            patient=self.patient,
            doctor=self.doctor,
        )

        url = reverse("mapping-list-create")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data),
            1,
        )

    def test_get_doctors_assigned_to_patient(self):
        PatientDoctorMapping.objects.create(
            patient=self.patient,
            doctor=self.doctor,
        )

        PatientDoctorMapping.objects.create(
            patient=self.patient,
            doctor=self.doctor_two,
        )

        url = reverse(
            "mapping-detail",
            kwargs={"pk": self.patient.id},
        )

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data),
            2,
        )

        doctor_ids = {
            mapping["doctor"]
            for mapping in response.data
        }

        self.assertIn(
            self.doctor.id,
            doctor_ids,
        )

        self.assertIn(
            self.doctor_two.id,
            doctor_ids,
        )

    def test_duplicate_mapping_fails(self):
        PatientDoctorMapping.objects.create(
            patient=self.patient,
            doctor=self.doctor,
        )

        url = reverse("mapping-list-create")

        response = self.client.post(
            url,
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

    def test_cannot_assign_doctor_to_another_users_patient(self):
        url = reverse("mapping-list-create")

        response = self.client.post(
            url,
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
            "mapping-detail",
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

    def test_cannot_delete_another_users_mapping(self):
        mapping = PatientDoctorMapping.objects.create(
            patient=self.other_patient,
            doctor=self.doctor,
        )

        url = reverse(
            "mapping-detail",
            kwargs={"pk": mapping.id},
        )

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

        self.assertTrue(
            PatientDoctorMapping.objects.filter(
                id=mapping.id
            ).exists()
        )