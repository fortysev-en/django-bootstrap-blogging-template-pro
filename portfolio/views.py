from urllib import request
from django.shortcuts import render, HttpResponse
from . import models

def index(response):
    if response.method == 'POST':
        name = response.POST['name']
        email = response.POST['email']
        desc = response.POST['desc']

        print(name, email, desc)
        con = models.Contact(name=name, email=email, desc=desc)
        con.save()

    return render(response, 'index.html')
