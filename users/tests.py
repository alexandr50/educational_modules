from unittest import mock

from django.core.files import File
from rest_framework import status
from rest_framework.test import APITestCase

from categories.models import Category
from educational_modules.models import EducationalModule
from .models import CustomUser



class CustomUserTestCase(APITestCase):

    def setUp(self) -> None:
        self.category = Category.objects.create(
            title='Languages'
        )
        self.ed_module = EducationalModule.objects.create(
            category=self.category,
            name="Test",
            description='description',
            price=1000,

        )
        self.file = mock.MagicMock(spec=File)
        self.file.name = 'test.txt'

    def test_create_user(self):
        """Тест создания юзера"""

        data = {
            'first_name': 'testfirst',
            'last_name': 'testlast',
            'email': 'emailtest@mail.ru',
            'educational_modules': self.ed_module.pk
        }

        response = self.client.post(
            '/users/create/',
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(CustomUser.objects.all().count(), 1)
        self.assertEqual(CustomUser.objects.all().first().first_name, 'testfirst')
        self.assertEqual(CustomUser.objects.all().first().email, 'emailtest@mail.ru')

    def test_delete_user(self):
        """Тест удаления юзера"""

        data = {
            'first_name': 'testfirst',
            'last_name': 'testlast',
            'email': 'emailtest@mail.ru',
        }
        usr = CustomUser.objects.create(**data)
        usr.educational_modules.set([3])

        response = self.client.delete(
            f'/users/delete/{usr.pk}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertEqual(CustomUser.objects.all().count(), 0)
        self.assertFalse(CustomUser.objects.filter(id=usr.id).exists())

    def test_update_user(self):
        """Тест обновления юзера"""

        data = {
            'first_name': 'testfirst',
            'last_name': 'testlast',
            'email': 'emailtest@mail.ru',
        }
        usr = CustomUser.objects.create(**data)

        usr.educational_modules.set([9])

        data_for_update = {
            'first_name': 'testfirst2',
            'last_name': 'testlast2',
            'email': 'emailtest@mail.ru',
            'educational_modules': self.ed_module.pk
        }

        response = self.client.patch(
            f'/users/update/{usr.pk}/',
            data=data_for_update
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(CustomUser.objects.get(id=usr.id).first_name, 'testfirst2')
        self.assertEqual(CustomUser.objects.get(id=usr.id).last_name, 'testlast2')
