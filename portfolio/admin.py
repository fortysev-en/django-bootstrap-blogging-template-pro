from django.contrib import admin

from django.contrib import admin
from portfolio.models import Contact, LikesModel, ViewsModel

# Register your models here.
admin.site.register(Contact)
admin.site.register(ViewsModel)
admin.site.register(LikesModel)
