from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import User
from .models import Patient


class PatientTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="patientuser@example.com",
            name="Patient User",
            password="TestPassword123!",
        )

        self.other_user = User.objects.create_user(
            email="other@example.com",
            name="Other User",
            password="TestPassword123!",
        )

        self.client.force_authenticate(user=self.user)

        self.patient_url = reverse("patient-list-create")

    def test_create_patient(self):
        data = {
            "name": "Alice Smith",
            "email": "alice@example.com",
            "phone": "+919999999999",
            "date_of_birth": "1995-05-15",
            "address": "Bangalore, India",
        }

        response = self.client.post(
            self.patient_url,
            data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Alice Smith")

        self.assertTrue(
            Patient.objects.filter(
                name="Alice Smith",
                created_by=self.user,
            ).exists()
        )

    def test_list_only_my_patients(self):
        Patient.objects.create(
            created_by=self.user,
            name="My Patient",
        )

        Patient.objects.create(
            created_by=self.other_user,
            name="Other Patient",
        )

        response = self.client.get(self.patient_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "My Patient")

    def test_unauthenticated_user_cannot_access_patients(self):
        self.client.force_authenticate(user=None)
        
        url = reverse("patient-list-create")

        response = self.client.get(url)

        self.assertIn(
            response.status_code,
            [
                status.HTTP_401_UNAUTHORIZED,
                status.HTTP_403_FORBIDDEN,
            ],
        )

    def test_update_patient(self):
        patient = Patient.objects.create(
            created_by=self.user,
            name="Old Name",
        )

        url = reverse(
            "patient-detail",
            kwargs={"pk": patient.id},
        )

        response = self.client.patch(
            url,
            {"name": "Updated Name"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Name")

    def test_delete_patient(self):
        patient = Patient.objects.create(
            created_by=self.user,
            name="Delete Me",
        )

        url = reverse(
            "patient-detail",
            kwargs={"pk": patient.id},
        )

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )

        self.assertFalse(
            Patient.objects.filter(id=patient.id).exists()
        )