from django.db import models

class SolarSystemObjects(models.Model):
    object_name = models.CharField("Название обьекта", unique=True, max_length=50)
    object_distance = models.CharField("Расстояние от Солнца", max_length=100, blank=True)
    object_introduction = models.CharField("Небольшое предисловие", max_length=250)
    object_description = models.TextField("Информация об обьекте", max_length=1500)
    object_image_main = models.ImageField("Фото обьекта для главной страницы", upload_to='media/object_image_main')
    object_image_d = models.ImageField("Фото обьекта для описания", upload_to='media/object_image_d')


    def __str__(self):
        return self.object_name


    class Meta:
        verbose_name = "Космический обьект"
        verbose_name_plural = "Космические обьекты"