import random
from django.shortcuts import render,redirect
from index.models import *
from project1 import settings
import datetime


# Create your views here.

def list_views(request):
    if 'uname' in request.session:
        uname = request.session['uname']
        user = Users.objects.filter(uname=uname).values('uname')
        uname = user[0]['uname']
        categories = Category.objects.all()
        # 按照id从低到高排列获取所有的博客信息
        topics = Topic.objects.all().order_by('-id')
        # 获取按照read_num从高到低排列的前三篇博客信息
        recommends = Topic.objects.all().order_by('read_num')[0:3]
        # 随机获取5篇博客
        topicfive = Topic.objects.all().values()
        results = random.sample(tuple(topicfive), 5)
        # 随机获取3篇文章
        topicthrees = random.sample(tuple(topicfive), 3)
        return render(request, 'list.html', locals())
    else:
        url = request.META.get('Referer', '/')
        return redirect(url,locals())

def taglist_views(request):
    # 标签搜索
    if request.method == 'GET':
        # 获取标签id
        topicid = request.GET['name']
        # 获取此标签所有文章
        topiclist = Topic.objects.filter(category_id=topicid).all()
        cates = Category.objects.filter(id=topicid).values('cate_name')
        return render(request,'taglist.html',locals())
