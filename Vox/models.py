from django.db import models
from django.forms import CharField


class Post(models.Model):
    name = models.CharField(max_length=122)
    quotes = models.CharField(max_length=200)
    # caption = models.CharField(max_length=500)
    # caption = models.ImageField((""), upload_to = None, width_field = None, max_length = None)
    date = models.DateTimeField()
    postimg = models.ImageField(
        upload_to="static/images", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']
