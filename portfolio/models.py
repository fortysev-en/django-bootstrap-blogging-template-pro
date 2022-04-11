from email.policy import default
from statistics import mode
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    desc = models.TextField()
    contacted_on = models.DateTimeField(auto_now_add=True)


class ViewsModel(models.Model):
    total_views = models.CharField(max_length=256)

    def __str__(self):
        return self.total_views


class LikesModel(models.Model):
    total_likes = models.CharField(max_length=256)

    def __str__(self):
        return self.total_likes