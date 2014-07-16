#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.core.urlresolvers import reverse
from django import forms
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.contrib.auth.models import User
 

class RegisterForm(forms.Form):
    username=forms.CharField(label=(u"注册账号"),widget=forms.TextInput(attrs={'placeholder':'输入注册账号'}))                                                                     
    email=forms.EmailField(label=(u"注册邮箱"),widget=forms.TextInput(attrs={'placeholder':'输入注册邮箱'}))                                                   
    password=forms.CharField(label=(u"密码"),widget=forms.PasswordInput(attrs={'placeholder':'输入6-12位密码'}))
    repassword=forms.CharField(label=(u"重复密码"),widget=forms.PasswordInput(attrs={'placeholder':'再次输入密码'}))

class LoginForm(forms.Form):
    name=forms.CharField(label=(u"账号"), widget=forms.TextInput(attrs={'placeholder':'输入注册账号'}))
    psd=forms.CharField(label=(u"密码"),widget=forms.PasswordInput(attrs={'placeholder':'输入注册密码'}))
                                                                               





def home(request):
    registerform=RegisterForm()
    loginform =LoginForm()
    return render_to_response('home.html',{'registerform':registerform,'loginform':loginform, })

def login(request):
    loginform = LoginForm()
    registerform=RegisterForm()
    if request.method == "POST":
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username=loginform.cleaned_data['name']
            password=loginform.cleaned_data['psd']
            user = auth.authenticate(username = username,password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                request.seesion['username']=user.username
                return render_to_response('home.html', RequestContext(request, {'loginform': loginform,'registerform':registerform}))  
            else:  
                return render_to_response('home.html', RequestContext(request, {'loginform': loginform,'registerform':registerform,'password_is_wrong':True}))  
        else:  
            return render_to_response('home.html', RequestContext(request, {'loginform': loginform,'registerform':registerform}))  



def register(request):
    loginform = LoginForm()
    if request.method=="POST":
        registerform=RegisterForm(request.POST)
        if registerform.is_valid():
            username = registerform.cleaned_data["username"]
            email = registerform.cleaned_data["email"]
            password = registerform.cleaned_data["password"]
            repassword = registerform.cleaned_data["repassword"]
            if password!= repassword:
                return HttpResponse('重复登录密码与登录密码不一致');
            user = User.objects.create_user(username, email, password)
            user.save()
    else:
        registerform=RegisterForm()
        
    return render_to_response('home.html',{'registerform':registerform,'loginform':loginform},context_instance=RequestContext(request))

def logout(request):
    registerform=RegisterForm()
    loginform =LoginForm()
    auth_logout(request)
    return render_to_response('home.html',{'registerform':registerform,'loginform':loginform},context_instance=RequestContext(request))


 
