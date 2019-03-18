from django.shortcuts import render,redirect
from index.models import *
from project1 import settings
import datetime

# Create your views here.

def time_views(request):
    if 'uname' in request.session:
        uname = request.session['uname']
        id = request.session['id']
        user = Users.objects.filter(uname=uname).values('uname')
        uname = user[0]['uname']
        topics = Topic.objects.filter(users_id=id).all()
        return render(request,'time.html',locals())
    else:
        url = request.META.get('Referer','/')
        return redirect(url)