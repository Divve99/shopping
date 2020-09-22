from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.urls import reverse
from sqlalchemy.sql.functions import mode

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=105)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured_post = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'id': self.id})
