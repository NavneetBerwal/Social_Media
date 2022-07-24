from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User


class Post(models.Model):
    name = models.CharField(max_length=122)
    quotes = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, blank = True)
    postimg = models.ImageField(
        upload_to="static/images", null=True, blank=True)
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Bio = models.CharField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return str(self.user)
    