from django.shortcuts import render,redirect
from index.models import *
from project1 import settings
import datetime

# Create your views here.

def gbook_views(request):
    if 'uname' in request.session:
        uname = request.session['uname']
        user = Users.objects.filter(uname=uname).values('uname')
        uname = user[0]['uname']
        return render(request,'gbook.html',locals())
    else:
        url = request.META.get('Referer','/')
        return redirect(url)