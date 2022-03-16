from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    desc = models.TextField()
