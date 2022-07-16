from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User


class Post(models.Model):
    name = models.CharField(max_length=122)
    quotes = models.CharField(max_length=200)
    # caption = models.CharField(max_length=500)
    # caption = models.ImageField((""), upload_to = None, width_field = None, max_length = None)
    date = models.DateTimeField(auto_now_add=True)
    postimg = models.ImageField(
        upload_to="static/images", null=True, blank=True)
    # likes = models.ManyToManyField(
    #     User, default=None, blank=True, related_name='Liked')
    # author = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name='auther')

    def __str__(self):
        return self.name

    # @property
    # def num_likes(self):
    #     return self.liked.all().count()

    class Meta:
        ordering = ['-date']


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)


class like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,
                             default='Like', max_length=10)

    def __str__(self):
        return str(self.post)
