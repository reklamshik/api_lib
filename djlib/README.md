# API for library
## Приложение позволяет получить доступ к информации о книгах, используя django-API

### Используемые urls:
1. api/books/ - информация по книгам
2. api/authors - информация по авторам

### Инструкция по локальной установке:
1. Установите текущую версию [Python](https://www.python.org/downloads/) с pip-менеджером.
2. Установите [git](https://git-scm.com/download/win) с командной строкой git-bash.
3. Склонируйте себе [рипозиторий](https://github.com/reklamshik/api_lib.git) командой `git clone`
4. Перейдите в папку с проектом по пути `api_lib/djlib`
5. Введите: `pip install pipenv`
6. Далее: `pipenv install`
7. Создайте БД, выполнив миграции командой: `python manage.py migrate`
8. Заполните базу данных.
9. Запустите сервер командой: `python manage.py runserver`

### По вопросам работы приложения:
[Алексей](https://t.me/reklamshik1983).
