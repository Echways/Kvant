from django.db import models

class News(models.Model):
    title = models.CharField('Заголовок', max_length=100, unique=True)
    description = models.TextField('Текст новости', unique=True)
    image = models.ImageField('Фото', upload_to='img/news')
    def __str__(self):
        return self.title

class Projects(models.Model):
    title = models.CharField('Заголовок', max_length=100, unique=True)
    description = models.TextField('Текст новости', unique=True)
    image = models.ImageField('Фото', upload_to='img/projects')
    def __str__(self):
        return self.title

class Achievments(models.Model):
    text = models.TextField('Достижение', unique=True)
    def __str__(self):
        return self.text