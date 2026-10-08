from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import User
from .models import Doctor


class DoctorTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="doctoruser@example.com",
            name="Doctor User",
            password="TestPassword123!",
        )

        self.client.force_authenticate(user=self.user)

        self.doctor_url = reverse("doctor-list-create")

    def test_create_doctor(self):
        data = {
            "name": "Dr. Sarah Wilson",
            "specialization": "Cardiology",
            "email": "sarah@example.com",
            "phone": "+919888888888",
        }

        response = self.client.post(
            self.doctor_url,
            data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(
            Doctor.objects.filter(
                name="Dr. Sarah Wilson"
            ).exists()
        )

    def test_list_doctors(self):
        Doctor.objects.create(
            name="Dr. John Smith",
            specialization="Neurology",
        )

        response = self.client.get(self.doctor_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_doctor(self):
        doctor = Doctor.objects.create(
            name="Dr. John Smith",
            specialization="Neurology",
        )

        url = reverse(
            "doctor-detail",
            kwargs={"pk": doctor.id},
        )

        response = self.client.patch(
            url,
            {"specialization": "Cardiology"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["specialization"],
            "Cardiology",
        )

    def test_delete_doctor(self):
        doctor = Doctor.objects.create(
            name="Dr. Delete",
            specialization="Dermatology",
        )

        url = reverse(
            "doctor-detail",
            kwargs={"pk": doctor.id},
        )

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )

        self.assertFalse(
            Doctor.objects.filter(id=doctor.id).exists()
        )