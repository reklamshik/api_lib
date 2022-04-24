
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from app_lib.serializers import AuthorSerializer, BookSerializer
from app_lib.models import Author, Book
from app_lib.set_pagination import SetAuthorViewPagination, SetBookViewPagination


class AuthorListView(ListModelMixin, GenericAPIView):
    
    serializer_class = AuthorSerializer
    pagination_class = SetAuthorViewPagination
    
    def get_queryset(self):
        queryset = Author.objects.all()
        author_name = self.request.query_params.get('name')
        if author_name:
            queryset = [item for item in queryset if author_name in str(item)]
        return queryset
    
    def get(self, request):
        return self.list(request)


class BookListView(ListModelMixin, GenericAPIView):
    
    serializer_class = BookSerializer
    pagination_class = SetBookViewPagination
    
    def get_queryset(self):
        
        queryset = Book.objects.all()
        
        author_name = self.request.query_params.get('name')
        if author_name:
            queryset = [
                item for item in queryset if author_name.capitalize() in str(item.author)
            ]
            
        
        book_title = self.request.query_params.get('title')
        
        if book_title:
            queryset = queryset.filter(title__icontains=book_title.capitalize())
            
        pages = self.request.query_params.get('pages_more_than')
        if pages:
            queryset = [item for item in queryset if item.pagination > int(pages)]

        pages = self.request.query_params.get('pages_less_than')
        if pages:
            queryset = [item for item in queryset if item.pagination < int(pages)]

        pages = self.request.query_params.get('pages')
        if pages:
            queryset = [item for item in queryset if item.pagination == int(pages)]
        
        return queryset
    
    def get(self, request):
        return self.list(request)
        



