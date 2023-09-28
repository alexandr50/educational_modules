from django.db import models

from educational_modules.models import EducationalModule


class Content(models.Model):
    name = models.CharField(max_length=40, verbose_name='название', blank=True, null=True)
    material = models.FileField(upload_to='materials/', verbose_name='Материал')
    educational_module = models.ManyToManyField(EducationalModule,
                                                verbose_name='Образовательный модуль',
                                                related_name='educational_module')

    def get_file_fields(self):
        return [{"label": field.verbose_name, "field": getattr(self, field.name)} for field in self._meta.get_fields()
                if isinstance(field, models.FileField)]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
