from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import User
from django.contrib.auth.hashers import check_password


class UserModelTest(TestCase):

    def test_user_creation(self):
        user = User.objects.create(
            username='testuser',
            password='password123'
        )
        self.assertTrue(isinstance(user, User))
        self.assertTrue(user.id)
        self.assertTrue(user.created_at)
        self.assertTrue(user.updated_at)
        self.assertNotEqual(user.password, 'password123')

    def test_password_hashing_on_save(self):
        password = 'password123'
        user = User(username='testuser', password=password)
        user.save()
        self.assertNotEqual(user.password, password)
        self.assertTrue(check_password(password, user.password))

    def test_user_str_method(self):
        user = User.objects.create(username='testuser', password='password123')
        self.assertEqual(str(user), user.username)

    def test_get_main_image_url(self):

        test_image_path = 'apps/users/image.png'  # path to the test image
        user = User.objects.create(username='testuser', password='password123')
        user.mainimg = SimpleUploadedFile(
            name='test_image.png',
            content=open(test_image_path, 'rb').read(),
            content_type='image/png'
        )
        user.save()
        self.assertIn('users/test_image.png', user.get_main_image_url())

