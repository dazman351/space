from django.db import models

class Planets(models.Model):
    planet_name = models.CharField("Название планеты", unique=True, max_length=50)
    planet_distance = models.CharField("Расстояние от Солнца", max_length=100)
    planet_introduction = models.CharField("Небольшое предисловие", max_length=250)
    planet_description = models.TextField("Информация о планете", max_length=1500)
    planet_image = models.ImageField("Фото планеты", upload_to='media/planets_image')
    planet_image_second = models.ImageField("Второе фото планеты", upload_to='media/planets_image_second')
    planet_image_main = models.ImageField("Фото для главной страницы", upload_to='media/planets_image_main')


    def __str__(self):
        return self.planet_name


    class Meta:
        verbose_name = "Планета"
        verbose_name_plural = "Планеты"
