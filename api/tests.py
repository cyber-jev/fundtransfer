from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class UserAPITest(APITestCase):

    def setUp(self):
        self.create_url = reverse("create-user")
        self.fund_url = reverse("fund-user")
        self.list_url = reverse("list-users")
        self.user_data = {
            "phone_number": "+1234567890",
            "username": "testuser",
            "password": "testpassword",
        }
        self.super_user = User.objects.create_user(
            phone_number="+1234567899",
            username="superuser",
            password="superpassword",
            is_staff=True,
        )

    def test_create_user(self):
        response = self.client.post(self.create_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_duplicate_phone_number(self):
        self.client.post(self.create_url, self.user_data)
        response = self.client.post(self.create_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_fund_user(self):
        self.client.post(self.create_url, self.user_data)
        fund_data = {"phone_number": "+1234567890", "amount": "100.00"}
        # self.client.login(username="superuser", password="superpassword")
        self.client.force_authenticate(user=self.super_user)
        response = self.client.post(self.fund_url, fund_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_users(self):
        # self.client.login(username="superuser", password="superpassword")
        self.client.force_authenticate(user=self.super_user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
