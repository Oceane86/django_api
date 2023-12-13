from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Bookmarks(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # champs manuels

    name = models.CharField(max_length=255)
    url = models.TextField()
    tags = models.TextField(blank=True)
    comment = models.TextField(blank=True)

    def __str__(self) :
        return self.name.upper() + " - " + self.url
    
    class Meta:
        """ diverses options """
        ordering = ['name']
        verbose_name = "Favori"
        verbose_name_plural = "Favoris"
