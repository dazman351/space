from django.db import models

class Articles(models.Model):
    name = models.CharField('Название статьи', max_length=100, unique=True)
    description = models.CharField('Описание статьи', max_length=500)
    full_text = models.TextField('Содержание статьи', max_length=5000)
    image_for_main = models.ImageField('Фото для статьи', upload_to='media/image_for_main')
    image_for_d = models.ImageField('Фото для содержания статьи', upload_to='media/image_for_d')
    time = models.DateTimeField('Время публикации', unique=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
