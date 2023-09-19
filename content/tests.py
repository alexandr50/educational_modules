from unittest import mock

from django.core.files import File
from rest_framework import status
from rest_framework.test import APITestCase

from categories.models import Category
from educational_modules.models import EducationalModule
from .models import Content


class ContentTestCase(APITestCase):

    def setUp(self) -> None:
        self.category = Category.objects.create(
            title='Languages'
        )
        self.ed_module = EducationalModule.objects.create(
            category=self.category,
            name="Test",
            description='description',
            price=1000

        )
        self.file = mock.MagicMock(spec=File)
        self.file.name = 'test.txt'

    def test_create_content(self):
        data = {
            'name': 'test1',
            'material': self.file,
            'educational_module': self.ed_module.pk
        }

        response = self.client.post(
            '/content/create/',
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(Content.objects.all().count(), 1)

    def test_delete_content(self):
        con = Content.objects.create(name='test1', material=self.file)
        con.educational_module.set([1])

        response = self.client.delete(
            f'/content/delete/{con.pk}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertEqual(Content.objects.all().count(), 0)
        self.assertFalse(Content.objects.filter(id=con.id).exists())

    def test_update_content(self):
        con = Content.objects.create(name='test1', material=self.file)
        con.educational_module.set([3])

        response = self.client.put(
            f'/content/update/{con.pk}/',
            data={
                'name': 'test1', 'material': self.file, 'educational_module': [3]
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(Content.objects.get(id=con.id).name, 'test1')
