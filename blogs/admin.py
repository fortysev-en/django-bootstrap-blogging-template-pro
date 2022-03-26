from django.contrib import admin
from . import models

admin.site.site_header = 'Fortyseven Admin'
admin.site.site_title = 'Fortyseven Admin Panel'
admin.site.index_title = 'Welcome to Fortyseven Admin Panel'

# Register your models here.
admin.site.register((models.Blog, models.BlogComment))
admin.site.register(models.ViewsModel)
admin.site.register(models.Profile)
