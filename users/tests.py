from django.test import TestCase

# Create your tests here.
from .models import User


# TEST USER MODEL
class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            phone_number="+1234567890", username="testuser", password="testpassword"
        )
        self.assertEqual(user.phone_number, "+1234567890")
        self.assertEqual(user.username, "testuser")

    def test_duplicate_phone_number(self):
        User.objects.create_user(
            phone_number="+1234567890", username="testuser", password="testpassword"
        )
        with self.assertRaises(Exception):
            User.objects.create_user(
                phone_number="+1234567890", username="testuser", password="testpassword"
            )
