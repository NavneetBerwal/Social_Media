from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
from PIL import Image

class Comment(models.Model):
    body = models.TextField()
    comname = models.TextField()
    cid = models.ForeignKey("Vox.Post", on_delete=models.CASCADE, null=True, blank=True)

class Post(models.Model):
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    quotes = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, blank=True)
    #comment = models.ForeignKey(Comment, on_delete=models.CASCADE,null= True, blank=True)
    postimg = models.ImageField(
        upload_to="static/images", null=True, blank=True)

    @property
    def num_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-date']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(default='default.jpg',
                              upload_to='profile_images')

    def __str__(self):
        return self.user.username


def save(self, *args, **kwargs):
    super().save()

    img = Image.open(self.avatar.path)

    if img.height > 100 or img.width > 100:
        new_img = (100, 100)
        img.thumbnail(new_img)
        img.save(self.avatar.path)

