from django.shortcuts import render
from django.http import HttpResponse
from app_lib.models import Author, Book
import random


def filling_db(request):
    pass
    # for i_book in range(1, 301):
    #     book = Book.objects.get(id=i_book)
    #     book.pagination=random.randint(25, 600)
    #     book.save()
    # title = ['Крепость', 'Петр первый', 'Война и мир', 'Зеленый фургон',
    #          'Изумрудный город', 'Справочник по Физике']
    # # last_names = ['Иванов', 'Петров', 'Сидоров', 'Кузнецов', 'Васнецов', 'Брыль']
    #
    #
    # for _ in range(300):
    #     Book.objects.create(title=random.choice(title),
    #                         isbn=random.randint(100, 1000),
    #                         publish_year=str(random.randint(1900, 2022)),
    #                         author=random.choice(Author.objects.all()))
    #
    #
    # return HttpResponse('База пополнена')