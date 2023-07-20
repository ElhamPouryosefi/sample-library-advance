from rest_framework import serializers

from apps.library.models.author import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'birth_date',)
