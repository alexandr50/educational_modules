# Generated by Django 4.2.5 on 2023-09-17 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_modules', '0001_initial'),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='educational_module',
            field=models.ManyToManyField(related_name='educational_module', to='educational_modules.educationalmodule', verbose_name='Образовательный модуль'),
        ),
    ]
