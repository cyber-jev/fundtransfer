from django.test import TestCase
from ..models import User


class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            phone_number="+1234567890", username="testuser", password="testpassword"
        )
        self.assertEqual(user.phone_number, "+12345678901")
        self.assertEqual(user.username, "+12345678901")

    def test_duplicate_phone_number(self):
        User.objects.create_user(
            phone_number="+1234567890", username="testuser", password="testpassword"
        )
        with self.assertRaises(Exception):
            User.objects.create_user(
                phone_number="+1234567890", username="testuser", password="testpassword"
            )
