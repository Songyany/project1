from django.shortcuts import render,redirect
from index.models import *
from project1 import settings
import datetime
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def photo_views(request):
    if 'uname' in request.session:
        id = request.session['id']
        user = Users.objects.filter(id=id).values('uname')
        uname = user[0]['uname']
        photos = Topic.objects.filter(users_id=id).all()
        pag = Paginator(photos, 12)
        page = request.GET.get('page',1)
        currentPage = int(page)
        try:
            # 获取当前页码
            photos = pag.page(page)
        except PageNotAnInteger:

            photos = pag.page(1)
        except EmptyPage:

            photos = pag.page(pag.num_pages)
        return render(request,'photo.html',locals())
    else:
        url = request.META.get('Referer', '/')
        return redirect(url,locals())




