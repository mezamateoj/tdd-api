"""Test for all the models in the app"""

from django.test import TestCase
from django.contrib.auth import get_user_model



class ModelTest(TestCase):
    """Test models."""

    def test_create_user_with_email_success(self):
        """Test creating a user with an email is successful"""

        email = 'test@example.com'
        password = 'test1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalized(self):
        """Test email is normalized for new users"""

        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@EXAMPLE.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_email_normalized_error(self):
        """Test creating user without email raises ValueError"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'tests')

    def test_create_superuser(self):
        """Test creating superuser"""

        user = get_user_model().objects.create_superuser(
            email='test@example.com',
            password='test1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


