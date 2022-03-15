
from django.shortcuts import render
from .models import *


def index(response):
    return render(response, 'index.html')
