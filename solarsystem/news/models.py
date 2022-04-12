from django.db import models

class News(models.Model):
    name = models.CharField('Название новости', max_length=100, unique=True)
    description = models.CharField('Описание новости', max_length=300)
    full_text = models.TextField('Содержание новости', max_length=5000)
    photo_for_main = models.ImageField('Фото для новости', upload_to='media/photo_for_main')
    photo_for_d = models.ImageField('Фото для содержания новости', upload_to='media/photo_for_d')
    time = models.DateTimeField('Время публикации', unique=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
