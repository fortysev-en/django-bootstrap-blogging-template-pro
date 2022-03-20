from urllib import response
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate


class LoginView(APIView):
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong!'

        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'Something went wrong!'
                raise Exception('Key username not found')

            if data.get('password') is None:
                response['message'] = 'Something went wrong!'
                raise Exception('Key password not found')
        
            
            check_user = User.objects.filter(username = data.get('username')).first()

            if check_user is None:
                response['message'] = 'Invalid Username'
                raise Exception('User not found')

            user_obj = authenticate(username = data.get('username'), password = data.get('password'))

            if user_obj:
                response['status'] = 200
                response['message'] = 'Welcome'
            else:
                response['message'] = 'Invalid Password'
                raise Exception('Inalid Password')
        
        
        except Exception as e:
            print(e)

        return Response(response)


LoginView = LoginView.as_view()



class SignupView(APIView):
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong!'

        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'Something went wrong!'
                raise Exception('Key username not found')

            if data.get('password') is None:
                response['message'] = 'Something went wrong!'
                raise Exception('Key password not found')
        
            
            check_user = User.objects.filter(username = data.get('username')).first()

            if check_user:
                response['message'] = 'Username already taken'
                raise Exception('Username already taken')

            user_obj = User.objects.create(username = data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            response['message'] = 'User created'
            response['status'] = 200
        
        
        except Exception as e:
            print(e)

        return Response(response)

SignupView = SignupView.as_view()