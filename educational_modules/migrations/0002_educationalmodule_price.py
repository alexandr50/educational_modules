# Generated by Django 4.2.5 on 2023-09-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_modules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationalmodule',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Стоимость'),
        ),
    ]