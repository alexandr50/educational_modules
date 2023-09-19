from rest_framework import status
from rest_framework.test import APITestCase

from categories.models import Category
from .models import EducationalModule


class EdModuleTestCase(APITestCase):

    def setUp(self) -> None:
        self.category = Category.objects.create(
            title='Languages'
        )

    def test_create_ed_module(self):
        """Тест создания модуля"""

        data = {
            'category': self.category.pk,
            'name': 'test1',
            'description': 'description_test1',
            'price': 1000
        }

        response = self.client.post(
            '/educational_modules/create/',
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(EducationalModule.objects.all().count(), 1)
        self.assertEqual(EducationalModule.objects.all().first().name, 'test1')
        self.assertEqual(EducationalModule.objects.all().first().price, 1000)

    def test_delete_ed_module(self):
        """Тест удаления контента"""

        data = {
            'category': self.category,
            'name': 'test1',
            'description': 'description_test1',
            'price': 1000
        }
        ed_mod = EducationalModule.objects.create(**data)

        response = self.client.delete(
            f'/educational_modules/delete/{ed_mod.pk}/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertEqual(EducationalModule.objects.all().count(), 0)
        self.assertFalse(EducationalModule.objects.filter(id=ed_mod.id).exists())

    def test_update_ed_module(self):
        """Тест обновления контента"""

        data = {
            'category': self.category,
            'name': 'test1',
            'description': 'description_test1',
            'price': 1000
        }
        ed_mod = EducationalModule.objects.create(**data)

        data_for_update = {
            'category': self.category,
            'name': 'test2',
            'description': 'description_test2',
            'price': 2000
        }

        response = self.client.patch(
            f'/educational_modules/update/{ed_mod.pk}/',
            data=data_for_update
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(EducationalModule.objects.get(id=ed_mod.id).price, 2000)
        self.assertEqual(EducationalModule.objects.get(id=ed_mod.id).name, 'test2')
