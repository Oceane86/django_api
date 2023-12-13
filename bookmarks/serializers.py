# bookmarks/serializers.py

from rest_framework import serializers
from .models import Bookmarks

class BooksmarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmarks
        fields = '__all__'
        # fields = ['id', 'name', 'url', 'tags']

