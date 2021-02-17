from django.shortcuts import render,redirect
from django.views import View
from django.forms import forms
from .forms import LoginForm,SignupForm,ForgotPasswordForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication, permissions
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth,User
from rest_framework.generics import GenericAPIView
from rest_framework import status
from django.conf import settings
import jwt
from .serializers import UserSerializer, LoginSerializer
from rest_framework import status
from django.http import JsonResponse
import json


class HelloView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class Login(APIView ):
    def get(self,request):
        login_form = LoginForm() 
        context = {'login_form':login_form}
        return render(request,'login.html',context)

    def post(self,request):
        # form = LoginForm(request.POST)
        # form_data_dict = {}
        # form_data_list = json.loads(form_data)
        # for field in form_data_list:
        #     form_data_dict[field["name"]] = field["value"]
        # return form_data_dict
        username = request.POST["username"]
        print(username)
        password = request.POST["password"]
        user = auth.authenticate(username=username,password= password)
        if user:
            auth_token = jwt.encode({'username':user.username},settings.JWT_SECRET_KEY)
            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token,'status':'success'}
            auth.login(request,user)
            print(data)
            # return redirect(home)
            response = JsonResponse(data, status=status.HTTP_200_OK)
            response.set_cookie('token', auth_token)
            return response
            
        else:
                # SEND RES
            return JsonResponse({'status': 'fail'},safe=False)
        # return get(request)     
        # else:
        #     return self.get(request)     


class Signup(View):
    def get(self,request):
        signup_form = SignupForm() 
        context = {'signup_form':signup_form}
        return render(request,'signup.html',context)
    def post(self,request):
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]
            User.objects.create_user(first_name=first_name,last_name=last_name,email=email,
                                    username=username,password=password)
            return redirect('login')
        else:
            return redirect('login')
    

def home(request):
    if request.user.is_authenticated:
        print('Homeee')

        return render(request,'home.html')
    else:
        return redirect('login')   

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        response = redirect('login')
        response.delete_cookie('token')
        return response

class reset_password(View):
    def get(self,request):
        forgot_password_form = ForgotPasswordForm() 
        context = {'forgot_password_form':forgot_password_form}
        return render(request,'forgot_password.html',context)    

    def post(self,request):
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
