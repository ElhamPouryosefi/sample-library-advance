from apps.library.models.book import Book
from apps.library.serializers.book import BookSerializer, AddBookRequestSerializer, BookBaseInfoSerializer
from core.library_modules.libray_generics import BookListCreateView, BookModifyView
from core.library_modules.view_handler import UserAPIView


class BookAPIView(BookListCreateView, UserAPIView):
    permission_name = {'GET': 'book.view_book', 'POST': 'book.add_book'}
    queryset = Book.objects.all()
    serializer_class = AddBookRequestSerializer
    ordering_fields = '__all__'

    def get_queryset(self):

        return super().get_queryset()

    def get_serializer_class(self):
        if self.request.method == 'GET' and not self.request.query_params.get('page'):
            return BookBaseInfoSerializer
        if self.request.method == 'GET':
            return BookSerializer
        return AddBookRequestSerializer


class ModifyBookAPIView(BookModifyView, UserAPIView):
    permission_name = {'GET': 'book.view_book', 'PUT': 'book.change_book', 'DELETE': 'book.delete_book'}
    queryset = Book.objects.all()
    serializer_class = AddBookRequestSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookSerializer
        return AddBookRequestSerializer

    def put(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)
        return response

