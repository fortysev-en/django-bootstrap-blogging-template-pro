from urllib import response
from django import views
from django.conf import settings
from django.shortcuts import redirect, render, HttpResponse
from .models import ViewsModel, Contact
from .forms import *
from django.contrib.auth import logout
from django.contrib import messages
from django.db.models import F
from .helpers import get_ip
import os
from datetime import datetime, date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import boto3


# Create your views here.
def homepage(request):
    context = {}

    ip = get_ip(request)

    if not ViewsModel.objects.filter(total_visits = ip).exists():
        ViewsModel.objects.create(total_visits = ip)
        
    # get total unique visitor count
    visitor_count = ViewsModel.objects.all().count()

    context['visitorCount'] = visitor_count
    context['blogs'] = Blog.objects.all()

    context['pendingReviewCount'] = Blog.objects.filter(is_approved = False).count()
    context['pendingMessageCount'] = Contact.objects.filter(is_viewed = False).count()

    return render(request, 'homepage.html', context)


def login(request):
    context = {}

    context['recaptcha_site_key'] = settings.GOOGLE_RECAPTCHA_SITE_KEY
    
    return render(request, 'login.html', context)

def my_profile(request):
    context = {}

    context['pendingReviewCount'] = Blog.objects.filter(is_approved = False).count()
    context['pendingMessageCount'] = Contact.objects.filter(is_viewed = False).count()

    userCommentData = BlogComment.objects.filter(user = request.user).all()
    context['userCommentData'] = userCommentData

    context['userTotalComments'] = userCommentData.count()

    userModel = User.objects.get(username = request.user)

    userProfile = Profile.objects.get(user = request.user)

    if request.user.is_superuser:
        context['userState'] = 'SUPERUSER'
    elif request.user.is_staff and not request.user.is_superuser:
        context['userState'] = 'Staff'
    else:
        context['userState'] = 'Viwer'

    s3 = boto3.client('s3', aws_access_key_id = settings.AWS_ACCESS_KEY_ID, aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY)

    if request.method == 'POST':
        userModel.first_name = request.POST.get('firstname')
        userModel.last_name = request.POST.get('lastname')
        userProfile.website_url = request.POST.get('personalWebsite')
        userProfile.github_url = request.POST.get('personalGithub')
        userProfile.facebook_url = request.POST.get('personalFacebook')
        userProfile.instagram_url = request.POST.get('personalInstagram')
        userProfile.twitter_url = request.POST.get('personalTwitter')

        img = request.FILES.get('profilePictureImg')
        if not img is None:
            if not userProfile.profilePicture:
                userProfile.profilePicture = request.FILES['profilePictureImg']
            else:
                try:
                    s3.delete_object(Bucket = f'{settings.AWS_STORAGE_BUCKET_NAME}',Key = f'{userProfile.profilePicture}')
                    userProfile.profilePicture = request.FILES['profilePictureImg']
                except:
                    messages.warning(request, f"Unable to update profile picture!")
        
        userProfile.save()
        userModel.save()

        messages.success(request, f"Profile updated successfully!")
        return redirect('/myProfile/')
        # request.POST.get('gist')

    return render(request, 'my-profile.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        con = Contact(name=name, email=email, desc=desc)
        con.save()

    return render(request, 'contact.html')

def logout_view(request):
    logout(request)
    messages.success(request, f"Logged out successfully!")
    return redirect('/')

def blog_detail(request, slug):
    context = {}
    
    ip = get_ip(request)

    context['pendingReviewCount'] = Blog.objects.filter(is_approved = False).count()
    context['pendingMessageCount'] = Contact.objects.filter(is_viewed = False).count()

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
        context['approvedAt'] = blog_obj.approved_at
        context['approvedBy'] = blog_obj.approved_by

    except Exception as e:
        print(e)

    return render(request, 'blog-detail.html', context)

def add_blog(request):
    context = {}

    if not (request.user.is_authenticated and request.user.is_staff):
            return redirect('/')
    else:
        context['pendingReviewCount'] = Blog.objects.filter(is_approved = False).count()
        context['pendingMessageCount'] = Contact.objects.filter(is_viewed = False).count()


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
                
                messages.success(request, f"Blog Added Successfully, Pending Review!")
                return redirect('/myBlogs/')

        except Exception as e:
            print(e)

        return render(request, 'add-blog.html', context)

def blog_update(request, pk):
    context = {}
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect('/')
    else:
        context['pendingReviewCount'] = Blog.objects.filter(is_approved = False).count()
        context['pendingMessageCount'] = Contact.objects.filter(is_viewed = False).count()

        s3 = boto3.client('s3', aws_access_key_id = settings.AWS_ACCESS_KEY_ID, aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY)

        try:
            blog_obj = Blog.objects.get(id = pk)
        
            if (request.user.is_superuser) or (blog_obj.user == request.user):
                initial_dict = {'content': blog_obj.content}
                form = BlogForms(initial = initial_dict)

                old_img = blog_obj.image.name

                if request.method == 'POST':
                    form = BlogForms(request.POST)
                    blog_obj.title = request.POST.get('title')
                    blog_obj.gist =  request.POST.get('gist')

                    # if not len(request.FILES['image']) == 0:
                    #     blog_obj.image = request.FILES['image']
                    #     os.remove(os.path.join(settings.MEDIA_ROOT, old_img))

                    img = request.FILES.get('image')
                    if not img is None:
                        # os.remove(os.path.join(settings.MEDIA_ROOT, old_img))
                        try:
                            s3.delete_object(Bucket = f'{settings.AWS_STORAGE_BUCKET_NAME}',Key = f'{old_img}')
                            blog_obj.image = request.FILES['image']
                        except:
                            messages.warning(request, f"Unable to update blog picture!")
        

                    if form.is_valid():
                        blog_obj.content = form.cleaned_data['content']

                    blog_obj.is_approved = False
                    blog_obj.save()

                    messages.success(request, f"Blog Updated Successfully, Pending Review!")
                    return redirect('/myBlogs/')
                
                context['blog_obj'] = blog_obj
                context['form'] = form
            else:
                return redirect('/')

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

        return redirect('/myBlogs/')

def my_blogs(request):
    context = {}
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect('/')
    else:
        context['pendingReviewCount'] = Blog.objects.filter(is_approved = False).count()
        context['pendingMessageCount'] = Contact.objects.filter(is_viewed = False).count()

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

    context['pendingReviewCount'] = Blog.objects.filter(is_approved = False).count()
    context['pendingMessageCount'] = Contact.objects.filter(is_viewed = False).count()

    if request.GET.get('search'):
        searchQuery = request.GET.get('search')
        searchBlogs = Blog.objects.filter(title__icontains=searchQuery)
        context['searchResults'] = searchBlogs
        context['searchQuery'] = searchQuery
        try:
            searchUsers = (User.objects.filter(username = searchQuery).all()) or (User.objects.filter(first_name = searchQuery).all()) or (User.objects.filter(last_name = searchQuery).all())
            context['searchUsers'] = searchUsers
        except Exception as e:
            print(e)

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


def user_profile(request, username):
    context = {}
    context['pendingReviewCount'] = Blog.objects.filter(is_approved = False).count()
    context['pendingMessageCount'] = Contact.objects.filter(is_viewed = False).count()

    usr = User.objects.get(username = username)

    userCommentData = BlogComment.objects.filter(user = usr).all()
    context['userCommentData'] = userCommentData

    context['userTotalComments'] = userCommentData.count()
    context['defaultImg'] = "{% static 'img/blog-assests/default-profile-img.svg' %}"

    if usr.is_superuser and usr.is_staff:
        context['userState'] = 'SUPERUSER'
    elif usr.is_staff:
        context['userState'] = 'Staff'
    else:
        context['userState'] = 'Viewer'

    context['userData'] = usr

    return render(request, 'user-profile.html', context)


def subscribe(request):
    if request.method == 'POST':
        emailAddress = request.POST.get('emailAddress')

        if not Subscription.objects.filter(email = emailAddress).exists():
            Subscription.objects.create(email = emailAddress)

    return HttpResponse()