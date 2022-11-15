from django.contrib.auth.models import User
from django.db import models

class Warrior(models.Model):
    name = models.CharField('Имя', max_length=255, null=True)
    specialization = models.CharField('Специализация', max_length=255)
    image = models.ImageField('Изображение', upload_to='resource', default='', blank=True, null=True)
    description = models.TextField('Описание', blank=True)
    created_data = models.DateTimeField('Дата создания', auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
