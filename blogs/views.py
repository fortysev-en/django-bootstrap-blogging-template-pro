from traceback import print_tb
from urllib import response
from django import views
from django.conf import settings
from django.shortcuts import redirect, render, HttpResponse
from .models import ViewsModel
from .forms import *
from django.contrib.auth import logout
from django.contrib import messages
from django.db.models import F
from .helpers import get_ip
import os

# Create your views here.
def Homepage(request):
    context = {}

    ip = get_ip(request)

    if not ViewsModel.objects.filter(total_visits = ip).exists():
        ViewsModel.objects.create(total_visits = ip)
        
    # get total unique visitor count
    visitor_count = ViewsModel.objects.all().count()

    context['visitorCount'] = visitor_count
    context['blogs'] = Blog.objects.all()

    return render(request, 'homepage.html', context)

def login(request):
    context = {}

    context['recaptcha_site_key'] = settings.GOOGLE_RECAPTCHA_SITE_KEY
    
    return render(request, 'login.html', context)


def user_profile(request):
    context = {}

    userCommentData = BlogComment.objects.filter(user = request.user).all()
    context['userCommentData'] = userCommentData

    context['userTotalComments'] = userCommentData.count()

    return render(request, 'user-profile.html', context)


def select_pro_pic(request):

    # image =  request.FILES['myfile']
    # print(image)

    return redirect('/user-profile.html/')

def logout_view(request):
    logout(request)
    messages.success(request, f"Logged out successfully!")
    return redirect('/')

def blog_detail(request, slug):
    context = {}
    
    ip = get_ip(request)

    try:
        blog_obj = Blog.objects.filter(slug = slug).first()
        context['blogs_obj'] = blog_obj

        if not ViewsModel.objects.filter(total_visits = ip).exists():
            ViewsModel.objects.create(total_visits = ip)
            blog_obj.views.add(ViewsModel.objects.get(total_visits = ip))
        else:
            blog_obj.views.add(ViewsModel.objects.get(total_visits = ip))

        comments = BlogComment.objects.filter(post=blog_obj)
        context['comments'] = comments
        # context['user'] = request.user

    except Exception as e:
        print(e)

    return render(request, 'blog-detail.html', context)

def add_blog(request):
    context = {}

    if not (request.user.is_authenticated and request.user.is_staff):
            return redirect('/')
    else:

        context['form'] = BlogForms

        try:
            if request.method == 'POST':
                form = BlogForms(request.POST)
                image = request.FILES['image']
                title = request.POST.get('title')
                gist =  request.POST.get('gist')
                user = request.user

                if form.is_valid():
                    content = form.cleaned_data['content']

                Blog.objects.create(user = user, title = title, gist = gist, content = content, image=image)
                
                messages.success(request, f"Blog added successfully!")
                return redirect('/my-blogs/')

        except Exception as e:
            print(e)

        return render(request, 'add-blog.html', context)

def blog_update(request, pk):
    context = {}
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect('/')
    else:
        try:
            blog_obj = Blog.objects.get(id = pk)
        
            if blog_obj.user != request.user:
                return redirect('/')
            
            initial_dict = {'content': blog_obj.content}
            form = BlogForms(initial = initial_dict)

            old_img = blog_obj.image.name

            if request.method == 'POST':
                form = BlogForms(request.POST)
                blog_obj.image = request.FILES['image']
                blog_obj.title = request.POST.get('title')
                blog_obj.gist =  request.POST.get('gist')

                if not len(request.FILES['image']) == 0:
                    os.remove(os.path.join(settings.MEDIA_ROOT, old_img))

                if form.is_valid():
                    blog_obj.content = form.cleaned_data['content']

                blog_obj.save()

                messages.success(request, f"Blog updated successfully!")
                return redirect('/my-blogs/')
            
            context['blog_obj'] = blog_obj
            context['form'] = form

        except Exception as e:
            print(e)

        return render(request, 'update-blog.html', context)

def blog_delete(request, id):
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect('/')
    else:
        try:
            blog_obj = Blog.objects.get(id = id)

            if blog_obj.user == request.user:
                os.remove(os.path.join(settings.MEDIA_ROOT, blog_obj.image.name))
                blog_obj.delete()
                messages.success(request, 'Blog deleted successfully!')

        except Exception as e:
            print(e)

        return redirect('/my-blogs/')

def my_blogs(request):
    context = {}
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect('/')
    else:
        try:
            blog_objs = Blog.objects.filter(user = request.user)
            context['blogs_obj'] = blog_objs

        except Exception as e:
            print(e)

        return render(request, 'my-blogs.html', context)

def signup(request):
    context = {}
    if (request.user.is_authenticated):
        return redirect('/')
    else:

        context['recaptcha_site_key'] = settings.GOOGLE_RECAPTCHA_SITE_KEY

        return render(request, 'signup.html', context)

def search(request):
    context = {}

    if request.GET.get('search'):
        searchQuery = request.GET.get('search')
        searchResults = Blog.objects.filter(title__icontains=searchQuery)
        context['searchResults'] = searchResults
        context['searchQuery'] = searchQuery

    return render(request, 'search-page.html', context)

def comment_delete(request, id):

    if request.method == 'POST':
        print('POST', id)

    co = BlogComment.objects.filter(serial = id)
    co.delete()

    return redirect('')

# def postLike(request, pk):
#     post_id = request.POST.get('blog-id')
#     post = Blog.objects.get(pk=post_id)
#     ip = get_client_ip(request)
#     if not IpModel.objects.filter(ip=ip).exists():
#         IpModel.objects.create(ip=ip)
#     if post.likes.filter(id=IpModel.objects.get(ip=ip).id).exists():
#         post.likes.remove(IpModel.objects.get(ip=ip))
#     else:
#         post.likes.add(IpModel.objects.get(ip=ip))
#     return HttpResponseRedirect(reverse('post_detail', args=[post_id]))