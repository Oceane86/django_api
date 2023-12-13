# bookmarks/urls.py

from django.urls import include, path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register('bookmarks', views.BookMarksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]