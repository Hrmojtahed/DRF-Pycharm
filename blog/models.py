from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Article(models.Model):
    author = models.ForeignKey(User, null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    content = models.TextField(blank=True)
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
