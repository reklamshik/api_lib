from django.db import models

from django.utils.timezone import localtime


class Author(models.Model):
    first_name = models.CharField(max_length=10, default='', verbose_name='Имя')
    last_name = models.CharField(max_length=20, default='', verbose_name='Фамилия')
    date_of_birth = models.DateTimeField(default=localtime, verbose_name='Дата рождения')
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    title = models.CharField(max_length=50, default='', verbose_name='Название')
    isbn = models.IntegerField(default=1)
    publish_year = models.CharField(max_length=4, default='', verbose_name='Год выпуска')
    pagination = models.IntegerField(default=1, verbose_name='Количество страниц')
    
    author = models.ForeignKey(Author, blank=True, default=None, on_delete=models.CASCADE)
    
    def author_name(self):
        return str(self.author)
    
    