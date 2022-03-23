from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *


class ViewsModel(models.Model):
    total_visits = models.CharField(max_length=256)

    def __str__(self):
        return self.total_visits

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=1000)
    gist = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='blogs')
    user = models.ForeignKey(User, blank=True , null=True , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    views = models.ManyToManyField(ViewsModel, related_name="post_views", blank=True)
    # likes = models.ManyToManyField(ViewsModel, related_name="post_likes", blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Blog, self).save(*args, **kwargs)

    def total_views(self):
        return self.views.count()

    # def total_likes(self):
    #     return self.likes.count()