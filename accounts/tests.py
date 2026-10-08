from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class AuthenticationTests(APITestCase):

    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")

        self.user_data = {
            "name": "Test User",
            "email": "test@example.com",
            "password": "TestPassword123!",
            "phone": "+919876543210",
        }

    def test_user_registration(self):
        response = self.client.post(
            self.register_url,
            self.user_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            User.objects.filter(email="test@example.com").exists()
        )

    def test_user_login_returns_jwt(self):
        User.objects.create_user(
            email="test@example.com",
            name="Test User",
            password="TestPassword123!",
        )

        response = self.client.post(
            self.login_url,
            {
                "email": "test@example.com",
                "password": "TestPassword123!",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_duplicate_email_registration_fails(self):
        User.objects.create_user(
            email="test@example.com",
            name="Existing User",
            password="TestPassword123!",
        )

        response = self.client.post(
            self.register_url,
            self.user_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)