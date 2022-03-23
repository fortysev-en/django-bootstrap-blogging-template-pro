from urllib import response
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import *
from django_email_verification import send_email
from django.conf import settings
import requests

class LoginView(APIView):
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong!'

        try:
            data = request.data
        
            check_user = User.objects.filter(username = data.get('username')).first()

            if check_user is None:
                response['message'] = 'Invalid Username/Password!'
                raise Exception('User not found')

            user_obj = authenticate(username = data.get('username'), password = data.get('password'))

            usr_name = data.get('username')

            if user_obj is None:
                response['message'] = 'Invalid Username/Password!'
                raise Exception('Invalid Password')
            else:
                login(request, user_obj)
                response['status'] = 200
                response['message'] = f'Welcome {usr_name}'
                messages.success(request, f"Welcome <b>{user_obj.first_name}</b>!")        
        
        except Exception as e:
            print(e)

        return Response(response)


LoginView = LoginView.as_view()



class SignupView(APIView):
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong!'

        dataRe = request.data
        recaptcha_response = dataRe.get('gReCaptcha')
        data = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        print(result)

        
        # try:
        #     data = request.data
        #     check_user = User.objects.filter(username = data.get('username')).first()
        #     check_email = User.objects.filter(email = data.get('username')).first()

        #     if check_user:
        #         response['message'] = 'User already exist!'
        #         raise Exception('User already exist!')
        #     elif check_email:
        #         response['message'] = 'Email already exist!'
        #         raise Exception('Email already exist!')
        #     else:
        #         usr = User.objects.create_user(first_name = data.get('firstname'), last_name = data.get('lastname'), email = data.get('email'), username = data.get('username'), password = data.get('password'))

        #         usr.is_active = False
        #         send_email(usr)

        #         response['message'] = f'Registration Successfull <b>{data.get("firstname")}</b>! Please verify your email address before using the service!'
        #         response['status'] = 200
        
        # except Exception as e:
        #     print(e)

        return Response(response)

SignupView = SignupView.as_view()
