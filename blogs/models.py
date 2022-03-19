from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    total_views = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Blog, self).save(*args, **kwargs)




class ViewsModel(models.Model):
    total_visits = models.CharField(max_length=256)

    def __str__(self):
        return self.total_visits
