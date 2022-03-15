from django.shortcuts import render, HttpResponse

def index(response):
    return render(response, 'index.html')
