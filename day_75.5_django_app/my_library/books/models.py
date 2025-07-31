# books/models.py
from django.db import models

class Book(models.Model):
    # The unique ID from the Google Books API
    google_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    published_date = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    cover_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title