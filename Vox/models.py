from django.db import models
from django.forms import CharField


class Post(models.Model):
    name = models.CharField(max_length=122)
    quotes = models.CharField(max_length=200)
    caption = models.CharField(max_length=500)
    date = models.DateTimeField()

    class Meta:
        ordering = ['-date']
