#coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from models import *
from django.db import models
# Create your views here.


def index(request):
    return render(request,'fresh/index.html')

def login(request):
    return render(request,'fresh/login.html')

def register(request):
    return render(request,'fresh/register.html')

def register2(request):
    User = UserInfo()
    dict=request.POST
    User.uname = dict.get('user_name')
    User.upwd = dict.get('cpwd')
    User.uemail = dict.get('email')
    User.save()
    return HttpResponse('saved success')

def login2(request):
    dict = request.POST
    uname1=dict.get('username')
    upwd1=dict.get('pwd')
    name = UserInfo.objects.filter(uname=uname1)
    pwd = UserInfo.objects.filter(upwd=upwd1)

    if len(name)==1:
        error_name=0
    else:
        error_name=1
    if len(pwd)==1:
        error_pwd=0
    else:
        error_pwd=1
    print(uname1,upwd1)
    print(name,pwd)
    print(error_name,error_pwd)
    context={'error_name':error_name,'error_pwd':error_pwd}
    if len(name)==1 and len(pwd)==1:
        context={'name':'chenggong','uname':uname1}
        return render(request,'fresh/index.html',context)
    else:
        return render(request,'fresh/login.html',context)

def user_center_info(request):
    return render(request,'fresh/user_center_info.html')

def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post=request.POST
        user.ushou=post.get('ushou')
        user.uaddress=post.get('uaddress')
        user.uyoubian=post.get('uyoubian')
        user.uphone=post.get('uphone')
        user.save()
    context={'title':'用户中心','user':user,'page_name':1}
    return render(request,'fresh/user_center_site.html',context)






