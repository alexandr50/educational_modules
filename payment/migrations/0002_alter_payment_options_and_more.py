# Generated by Django 4.2.5 on 2023-09-30 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('educational_modules', '0004_delete_usermodule'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'Платеж', 'verbose_name_plural': 'Платежи'},
        ),
        migrations.AlterField(
            model_name='payment',
            name='educational_module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educational_modules.educationalmodule', verbose_name='Образовательный модуль'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='покупатель'),
        ),
    ]