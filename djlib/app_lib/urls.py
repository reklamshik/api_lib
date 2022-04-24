from django.urls import path
from app_lib.api import AuthorListView, BookListView
from app_lib.views import filling_db


urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('books/', BookListView.as_view(), name='books'),
    path('fill/', filling_db)
]
