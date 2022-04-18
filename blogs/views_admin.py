from multiprocessing import context
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from datetime import datetime, date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from django_email_verification import send_email


def activate_user(request, pk):
    usr = User.objects.get(pk = pk)
    usr.is_active = True
    usr.save()
    return redirect('/adminView/userManage/')


def disable_user(request, pk):
    usr = User.objects.get(pk = pk)
    usr.is_active = False
    usr.save()
    return redirect('/adminView/userManage/')


def change_pwd(request, pk):
    return redirect('/adminView/userManage/')


def delete_user(request, pk):
    usr = User.objects.get(pk = pk)
    usr.delete()
    return redirect('/adminView/userManage/')


def resend_verification(request, pk):
    usr = User.objects.get(pk = pk)
    send_email(usr)
    return redirect('/adminView/userManage/')

def review_blog(request):
    context = {}
    if request.user.is_superuser:
        context['pendingReviewCount'] = Blog.objects.filter(is_ready_for_review = True).count()
        context['pendingMessageCount'] = Contact.objects.filter(is_viewed = False).count()

        readyForReview = Blog.objects.filter(is_ready_for_review = True)
        context['readyForReview'] = readyForReview
        # context['pendingReviewCount'] = Blog.objects.filter(is_ready_for_review = True).count()
 
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
        context['pendingReviewCount'] = Blog.objects.filter(is_ready_for_review = True).count()
        context['pendingMessageCount'] = Contact.objects.filter(is_viewed = False).count()

        usersList = User.objects.all().order_by('-date_joined')
        
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


def admin_messages(request):
    context = {}

    if request.user.is_superuser:
        context['pendingReviewCount'] = Blog.objects.filter(is_ready_for_review = True).count()
        context['pendingMessageCount'] = Contact.objects.filter(is_viewed = False).count()

        allMessages = Contact.objects.all().order_by('contacted_on')
        context['allMessages'] = allMessages
        # pendingMessageList = Contact.objects.filter(is_viewed = False).count()
        
        page = request.GET.get('page', 1)

        paginator = Paginator(allMessages, 15)
        try:
            pendingMessageList = paginator.page(page)
        except PageNotAnInteger:
            pendingMessageList = paginator.page(1)
        except EmptyPage:
            pendingMessageList = paginator.page(paginator.num_pages)

        context['messageList'] = pendingMessageList

        return render(request, 'admin-messages.html', context)
    else:
        return redirect('/')


# def mark_message(request, pk):
    
#     msg = Contact.objects.get(pk = pk)

#     if msg.is_viewed:
#         msg.is_viewed = False
#     else:
#         msg.is_viewed = True
#     msg.save()

#     return redirect('/adminView/adminMessages/')


def mark_msg(request):
    if request.method == 'POST':
        msgId = request.POST.get('id')
        msg = Contact.objects.get(pk = msgId)

        if msg.is_viewed:
            msg.is_viewed = False
        else:
            msg.is_viewed = True
        msg.save()

    return HttpResponse()


def delete_msg(request):
    if request.method == 'POST':
        msgId = request.POST.get('id')
        msg = Contact.objects.filter(pk = msgId)
        msg.delete()

    return HttpResponse()


def publish_blog(request, pk):
    blogForApproval = Blog.objects.get(id = pk)
    blogForApproval.is_approved = True
    blogForApproval.is_ready_for_review = False
    blogForApproval.approved_at = datetime.now().strftime('%b %d, %Y %I:%M %p')
    blogForApproval.approved_by = str(request.user.first_name)
    blogForApproval.save()
    messages.success(request, 'Blog Published Successfully!')
    
    return redirect('/adminView/reviewBlog/')


def admin_panel(request):
    context = {}
    if request.user.is_superuser:
        context['pendingReviewCount'] = Blog.objects.filter(is_ready_for_review = True).count()
        context['pendingMessageCount'] = Contact.objects.filter(is_viewed = False).count()

        return render(request, 'admin-panel.html', context)
    else:
        return redirect('/')


def user_subscriptions(request):
    context = {}

    if request.user.is_superuser:
        context['pendingReviewCount'] = Blog.objects.filter(is_ready_for_review = True).count()
        context['pendingMessageCount'] = Contact.objects.filter(is_viewed = False).count()

        allSubscriptions = Subscription.objects.all()
        context['allSubscriptions'] = allSubscriptions
        
        page = request.GET.get('page', 1)

        paginator = Paginator(allSubscriptions, 15)
        try:
            SubscriptionList = paginator.page(page)
        except PageNotAnInteger:
            SubscriptionList = paginator.page(1)
        except EmptyPage:
            SubscriptionList = paginator.page(paginator.num_pages)

        context['subscriptionList'] = SubscriptionList

        return render(request, 'admin-subscriptions.html', context)
    else:
        return redirect('/')