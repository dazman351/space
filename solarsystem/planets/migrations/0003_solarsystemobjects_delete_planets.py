# Generated by Django 4.0.2 on 2022-03-25 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0002_alter_planets_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolarSystemObjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_name', models.CharField(max_length=50, unique=True, verbose_name='Название обьекта')),
                ('object_distance', models.CharField(blank=True, max_length=100, verbose_name='Расстояние от Солнца')),
                ('object_introduction', models.CharField(max_length=250, verbose_name='Небольшое предисловие')),
                ('object_description', models.TextField(max_length=1500, verbose_name='Информация об обьекте')),
                ('object_image_main', models.ImageField(upload_to='media/object_image_main', verbose_name='Фото обьекта для главной страницы')),
                ('object_image_d', models.ImageField(upload_to='media/object_image_d', verbose_name='Фото обьекта для описания')),
            ],
            options={
                'verbose_name': 'Космический обьект',
                'verbose_name_plural': 'Космические обьекты',
            },
        ),
        migrations.DeleteModel(
            name='Planets',
        ),
    ]
