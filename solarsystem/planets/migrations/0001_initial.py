# Generated by Django 4.0.2 on 2022-03-24 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planet_name', models.CharField(max_length=50, unique=True, verbose_name='Название планеты')),
                ('planet_distance', models.CharField(max_length=100, verbose_name='Расстояние от Солнца')),
                ('planet_introduction', models.CharField(max_length=250, verbose_name='Небольшое предисловие')),
                ('planet_description', models.TextField(max_length=1500, verbose_name='Информация о планете')),
                ('planet_image', models.ImageField(upload_to='media/object_image_d', verbose_name='Фото планеты')),
                ('planet_image_second', models.ImageField(upload_to='media/planets_image_second', verbose_name='Второе фото планеты')),
                ('planet_image_main', models.ImageField(upload_to='media/object_image_main', verbose_name='Фото для главной страницы')),
            ],
        ),
    ]
