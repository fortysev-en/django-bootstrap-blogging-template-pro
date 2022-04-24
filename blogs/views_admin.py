from multiprocessing import context
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from datetime import datetime, date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from django_email_verification import send_email
from django.conf import settings
import boto3
import os
from django.contrib.auth import update_session_auth_hash

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


def admin_user_profile(request, username):
    if request.user.is_superuser:
        context = {}

        context['pendingReviewCount'] = Blog.objects.filter(is_ready_for_review = True).count()
        context['pendingMessageCount'] = Contact.objects.filter(is_viewed = False).count()

        userModel = User.objects.get(username = username)
        context['userModel'] = userModel

        userCommentData = BlogComment.objects.filter(user = userModel.pk).all()

        userPro = Profile.objects.filter(user = userModel)
        if len(userPro) == 0:
            Profile.objects.create(user = userModel)
        userProfile = Profile.objects.get(user = userModel)

        context['userCommentData'] = userCommentData
        context['userTotalComments'] = userCommentData.count()

        if userModel.is_superuser:
            context['userState'] = 'SUPERUSER'
        elif userModel.is_staff and not userModel.is_superuser:
            context['userState'] = 'Staff'
        else:
            context['userState'] = 'Viwer'

        if not settings.DEBUG:
            s3 = boto3.client('s3', aws_access_key_id = settings.AWS_ACCESS_KEY_ID, aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY)

        if request.method == 'POST':
            if request.POST.get("form_type") == 'formTabOne':
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
                        if not settings.DEBUG:
                            try:
                                s3.delete_object(Bucket = f'{settings.AWS_STORAGE_BUCKET_NAME}',Key = f'{userProfile.profilePicture}')
                                userProfile.profilePicture = request.FILES['profilePictureImg']
                            except:
                                messages.warning(request, f"Unable to update profile picture!")
                        else:
                            try:
                                os.remove(os.path.join(settings.MEDIA_ROOT, userProfile.profilePicture))
                                userProfile.profilePicture = request.FILES['profilePictureImg']
                            except:
                                messages.warning(request, f"Unable to update profile picture!")
                
                userProfile.save()
                userModel.save()

                messages.success(request, f"Profile updated successfully!")
                return render('/myProfile/')
            
            elif request.POST.get("form_type") == 'formTabThree':
                newPassword = request.POST.get('newPassword')
                confirmNew = request.POST.get('confirmNewPassword')

                if not newPassword == confirmNew:
                    messages.warning(request, 'Confirm Passwords does not match!')
                    usr = User.objects.get(username = userModel)
                    usr.set_password(newPassword)
                    usr.save()
                    messages.success(request, 'Password Changed Successfully!')
    else:
        return redirect('/')   

    return render(request, 'admin-user-profile.html', context)


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