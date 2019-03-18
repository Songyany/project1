from django.shortcuts import render
import datetime
import os
import random

from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from werkzeug.security import generate_password_hash, check_password_hash
from project1 import settings
from index.models import *
# Create your views here.

# def login_views(request):
#     # global categories, topics, recommends, results, labels, topicthrees
#     if request.method == 'GET':
#         # 获取请求原地址
#         url = request.META.get('HTTP_REFERER','/')
#         # 存入session
#         request.session['url']=url
#         # 判断session中有没有信息
#         if 'id' in request.session and 'uname' in request.session:
#             id = request.session['id']
#             user1 = Users.objects.filter(id=id).values('uname')
#             uname = user1[0]['uname']
#             categories = Category.objects.all()
#             # 按照id从低到高排列获取所有的博客信息
#             topics = Topic.objects.all().order_by('-id')
#             # 获取按照read_num从高到低排列的前三篇博客信息
#             recommends = Topic.objects.all().order_by('read_num')[0:3]
#             # 随机获取5篇博客
#             topicfive = Topic.objects.all().values()
#             results = random.sample(tuple(topicfive), 5)
#             # 随机获取12个标签
#             labels = random.sample(tuple(categories), 12)
#             # 随机获取3篇文章
#             topicthrees = random.sample(tuple(topicfive), 3)
#
#             return render(request,'login.html',locals())
#         else:
#             # 判断cookies中是否有信息
#             if 'id' in request.COOKIES and 'uname' in request.COOKIES:
#                 id = request.COOKIES['id']
#                 uname = request.COOKIES['uname']
#                 users = Users.objects.filter(id=id)
#                 # print(users)
#                 if users:
#                     # 如果正确，保存回session
#                     request.session['id']= id
#                     request.session['uname']= uname
#                     return render(request,'index.html')
#                     #　如果不正确，删除cookie中的信息
#                 else:
#                     resp = render(request,'login.html')
#                     resp.delete_cookie('id')
#                     resp.delete_cookie('uname')
#                     return resp
#             else:
#                 # 如果cookies中没有信息，返回登录界面
#                 return render(request,'login.html')
#     else:
#         # 获取输入信息，验证
#         uname = request.POST['uname']
#         upwd = request.POST['upwd']
#         user = Users.objects.filter(uname=uname).values('id','upwd')
#         # 如果正确，存入session
#         if user and check_password_hash(user[0]['upwd'],upwd):
#             request.session['id']=user[0]['id']
#             request.session['uname']=uname
#             # 从session中获取源地址
#             url = request.session['url']
#             resp = redirect(url)
#             expire = 60*60*24*1
#             resp.set_cookie('id', user[0]['id'],expire)
#             resp.set_cookie('uname',uname,expire)
#             return resp
#         else:
#             # 不正确则返回登录页
#             return render(request,'login.html',{'errMsg':'用户名或密码错误'})

def login_views(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        # 获取输入信息，验证
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        user = Users.objects.filter(uname=uname).values('id','upwd')
        # 如果正确，存入session
        if user and check_password_hash(user[0]['upwd'],upwd):
            request.session['id']=user[0]['id']
            request.session['uname']=uname
            categories = Category.objects.all()
            # 按照id从低到高排列获取所有的博客信息
            # topics = Topic.objects.all().order_by('-id')
            # # 获取按照read_num从高到低排列的前三篇博客信息
            # recommends = Topic.objects.all().order_by('read_num')[0:3]
            # # 随机获取5篇博客
            # topicfive = Topic.objects.all().values()
            # results = random.sample(tuple(topicfive), 5)
            # # 随机获取12个标签
            # labels = random.sample(tuple(categories), 12)
            # # 随机获取3篇文章
            # topicthrees = random.sample(tuple(topicfive), 3)
            return render(request,'index.html',locals())

def register_views(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        # 如果是post
        uname = request.POST['uname']
        users = Users.objects.filter(uname=uname)
        if users:
            # uname已存在
            return render(request,'register.html',{'errMsg':'用户已存在'})
        else:
            # 如果不存在则取值保存到数据库
            users = Users()
            users.uname = request.POST['uname']
            users.uemail = request.POST['uemail']
            users.uurl = request.POST['uurl']
            users.upwd = request.POST['upwd']
            users.upwd = generate_password_hash(users.upwd)
            # 保存会数据库
            try:
                users.save()
                return redirect('/')
            except Exception as ex:
                print(ex)
                return render(request,'register.html',{'errMsg':'请联系管理员'})

def loginout_views(request):
    url = request.META.get('HTTP_REFERER','/')
    if 'id' in request.session and 'uname' in request.session:
        del request.session['id']
        del request.session['uname']
        return redirect(url)