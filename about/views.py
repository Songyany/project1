from django.shortcuts import render,redirect
from index.models import *
from project1 import settings
import datetime

# Create your views here.

def about_views(request):
    if 'uname' in request.session:
        uname = request.session['uname']
        user = Users.objects.filter(uname=uname).values('uname')
        uname = user[0]['uname']
        return render(request,'about.html',locals())
    else:
        url = request.META.get('Referer','/')
        return redirect(url)

def aboutme_views(request):
    # 查询作者
    if request.method == 'GET':
        # 获取文章id
        topicid = request.GET['id']
        # 得到作者id
        topic = Topic.objects.filter(id=topicid).values('users_id')
        topiclist = Topic.objects.filter(users_id=topic).all()
        # 获取作者名字
        authors = Users.objects.filter(id=topic).values('uname')
        return render(request,'about.html',locals())