from django.shortcuts import render
from . import models

context = {}

# Create your views here.
def blogHomepage(request):

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

    if not models.ViewsModel.objects.filter(total_visits = ip).exists():
        models.ViewsModel.objects.create(total_visits = ip)

    # get total unique visitor count
    visitor_count = models.ViewsModel.objects.all().count()
    context['visitorCount'] = visitor_count


    return render(request, 'blog-homepage.html', context)