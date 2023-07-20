from rest_framework import serializers

from apps.authentication.models.custom_user import CustomUser
from apps.library.models.book import Book


class BookBaseInfoSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = Book
        fields = ('book_name', 'author', 'rate')


class BookSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = Book
        fields = ('book_name', 'author', 'pages', 'rate')


class AddBookRequestSerializer(serializers.Serializer):
    book_name = serializers.CharField()
    author = serializers.CharField()
    pages = serializers.IntegerField()
    rate = serializers.CharField()
