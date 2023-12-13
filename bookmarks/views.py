# Bookmarks/views.py

# from django.shortcuts import render

from rest_framework import viewsets

from .serializers import BooksmarksSerializer
from .models import Bookmarks

from rest_framework import filters


# Create your views here.


class BookMarksViewSet(viewsets.ModelViewSet):
    queryset = Bookmarks.objects.all().order_by('name')
    serializer_class = BooksmarksSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'content', 'tags']
    ordering_fields = ['name', 'content', 'tags']


