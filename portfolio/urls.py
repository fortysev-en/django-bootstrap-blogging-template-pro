from unicodedata import name
from django import views
from django.contrib import admin
from portfolio import views
from django.urls import path, include

app_name = 'portfolio'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='portfolio'),
    path('portfolio/contact', views.contact, name='contact'),
    path('portfolio/likes', views.likes, name='likes'),
]
