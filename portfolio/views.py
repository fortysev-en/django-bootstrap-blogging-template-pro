from urllib import request
from django.shortcuts import render, HttpResponse
from . import models

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        con = models.Contact(name=name, email=email, desc=desc)
        con.save()
        # success = f'Message successfully sent {name}!'

        return HttpResponse()