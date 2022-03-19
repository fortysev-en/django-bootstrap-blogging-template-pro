from tkinter import StringVar
from urllib import request
from django import views
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse, reverse
from . import models

context = {'isIpInDb' : 'False'}

def index(request):

    #get IP address of a user and save it in a model
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        print ("returning FORWARDED_FOR")
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        print ("returning REAL_IP")
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        print ("returning REMOTE_ADDR")
        ip = request.META.get('REMOTE_ADDR')

    if not models.ViewsModel.objects.filter(total_views = ip).exists():
        models.ViewsModel.objects.create(total_views = ip)
        
    if models.LikesModel.objects.filter(total_likes = ip).exists():
        context['isIpInDb'] = 'True'
    else:
        context['isIpInDb'] = 'False'

    # get total unique visitor count
    visitor_count = models.ViewsModel.objects.all().count()
    context['viewsCount'] = visitor_count

    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        con = models.Contact(name=name, email=email, desc=desc)
        con.save()
        # success = f'Message successfully sent {name}!'

        return HttpResponse()


def likes(request):
    global context

    if request.method == 'POST':
        #get IP address of a user and save it in a model
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            print ("returning FORWARDED_FOR")
            ip = x_forwarded_for.split(',')[-1].strip()
        elif request.META.get('HTTP_X_REAL_IP'):
            print ("returning REAL_IP")
            ip = request.META.get('HTTP_X_REAL_IP')
        else:
            print ("returning REMOTE_ADDR")
            ip = request.META.get('REMOTE_ADDR')

        
        if models.LikesModel.objects.filter(total_likes = ip).exists():
            models.LikesModel.objects.filter(total_likes = ip).delete()
            context['isIpInDb'] = 'False'
        else:
            models.LikesModel.objects.create(total_likes = ip)
            context['isIpInDb'] = 'True'

        return HttpResponse()
