from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='portfolio')
]
