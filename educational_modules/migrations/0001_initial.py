# Generated by Django 4.2.5 on 2023-09-17 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Стоимость')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Образовательный модуль',
                'verbose_name_plural': 'Образовательные модули',
            },
        ),
    ]
