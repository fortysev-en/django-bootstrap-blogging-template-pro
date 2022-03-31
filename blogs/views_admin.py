from django.http import HttpRequest
from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from datetime import datetime, date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *


def activate_user(request, pk):
    usr = User.objects.get(pk = pk)
    usr.is_active = True
    usr.save()
    # messages.success(request, 'User Activated Successfully!')
    return redirect('/adminView/userManage/')


def disable_user(request, pk):
    usr = User.objects.get(pk = pk)
    usr.is_active = False
    usr.save()
    # messages.success(request, 'User Disabled Successfully!')
    return redirect('/adminView/userManage/')


def change_pwd(request, pk):
    print('change_pwd', pk)
    return redirect('/adminView/userManage/')


def delete_user(request, pk):
    usr = User.objects.get(pk = pk)
    print('delete_user', pk)
    return redirect('/adminView/userManage/')


def review_blog(request):
    context = {}
    if request.user.is_superuser:
        context['pending_approval'] = Blog.objects.filter(is_approved = False)
        
        # page = request.GET.get('page', 1)

        # paginator = Paginator(usersList, 2)
        # try:
        #     users = paginator.page(page)
        # except PageNotAnInteger:
        #     users = paginator.page(1)
        # except EmptyPage:
        #     users = paginator.page(paginator.num_pages)
        return render(request, 'admin-review-blog.html', context)
    else:
        return redirect('/')


def user_manage(request):
    context = {}

    if request.user.is_superuser:
        context['pending_approval'] = Blog.objects.filter(is_approved = False)
        usersList = User.objects.all()
        
        page = request.GET.get('page', 1)

        paginator = Paginator(usersList, 15)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)

        context['usersList'] = users

        return render(request, 'admin-user-management.html', context)
    else:
        return redirect('/')


def publish_blog(request, pk):

    blogForApproval = Blog.objects.get(id = pk)
    blogForApproval.is_approved = True
    blogForApproval.approved_at = datetime.now().strftime('%b %d, %Y %I:%M %p')
    blogForApproval.approved_by = str(request.user.first_name)
    blogForApproval.save()
    messages.success(request, 'Blog Published Successfully!')
    
    return redirect('/admin-panel/')


def admin_panel(request):
    if request.user.is_superuser:
        return render(request, 'admin-panel.html')
    else:
        return redirect('/')