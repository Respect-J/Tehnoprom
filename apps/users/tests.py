from django.contrib.auth.hashers import check_password
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from .models import UserModel


class UserModelTest(TestCase):
    def setUp(self) -> None:
        photo = SimpleUploadedFile(name="test_image.jpg", content="", content_type="image/jpeg")
        self.user = UserModel.objects.create(username="testuser", password="password123", mainimg=photo)

    def test_user_creation(self):
        self.assertTrue(isinstance(self.user, UserModel))
        self.assertTrue(self.user.id)
        self.assertTrue(self.user.created_at)
        self.assertTrue(self.user.updated_at)
        self.assertNotEqual(self.user.password, "password123")

    def test_password_hashing_on_save(self):
        self.assertNotEqual(self.user.password, "password123")
        self.assertTrue(check_password("password123", self.user.password))

    def test_user_str_method(self):
        self.assertEqual(str(self.user), self.user.username)

    def test_get_main_image_url(self):
        self.assertIn("users/test_image", self.user.get_main_image_url())
