from django.contrib import admin

# Register your models here.

from bookmarks import models

admin.site.register(models.Bookmarks)