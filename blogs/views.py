from django.shortcuts import redirect, render
from .models import ViewsModel
from .forms import *

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

    if not ViewsModel.objects.filter(total_visits = ip).exists():
        ViewsModel.objects.create(total_visits = ip)

    # get total unique visitor count
    visitor_count = ViewsModel.objects.all().count()
    context['visitorCount'] = visitor_count


    return render(request, 'blog-homepage.html', context)


def login(request):
    return render(request, 'login.html')

def add_blog(request):
    context = {'form' : BlogForms}

    try:
        if request.method == 'POST':
            form = BlogForms(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']

            Blog.objects.create(user = user, title = title, content = content, image = image)

            return redirect('/add-blog/')

    except Exception as e:
        print(e)

    return render(request, 'add-blog.html', context)

def signup(request):
    return render(request, 'signup.html')
