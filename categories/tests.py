from rest_framework import status
from rest_framework.test import APITestCase

from .models import Category


class CategoryTestCase(APITestCase):
    def test_create_category(self):
        data = {
            'title': 'Languages'
        }

        response = self.client.post(
            '/categories/create/',
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(Category.objects.all().count(), 1)
        self.assertEqual(Category.objects.all().first().title, 'Languages')

    def test_delete_category(self):
        data = {
            'title': 'Languages'
        }
        cat = Category.objects.create(**data)

        response = self.client.delete(
            f'/categories/delete/{cat.pk}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertEqual(Category.objects.all().count(), 0)
        self.assertFalse(Category.objects.filter(id=cat.id).exists())

    def test_update_category(self):
        data = {
            'title': 'Languages'
        }
        cat = Category.objects.create(**data)

        data_for_update = {
            'title': 'Foreign languages'
        }

        response = self.client.put(
            f'/categories/update/{cat.pk}/',
            data=data_for_update
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(Category.objects.filter(id=cat.id).first().title, 'Foreign languages')
