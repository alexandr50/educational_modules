from django.db import models

from educational_modules.models import EducationalModule


class Content(models.Model):
    material = models.FileField(upload_to='materials/', verbose_name='Материал')
    educational_module = models.ManyToManyField(EducationalModule, verbose_name='Образовательный модуль')