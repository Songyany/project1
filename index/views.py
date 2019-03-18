
import random

from django.shortcuts import render
from . models import *
# Create your views here.



def index(request):
    # 获取所有的博客分类
    categories = Category.objects.all()
    # 按照id从低到高排列获取所有的博客信息
    topics = Topic.objects.all().order_by('-id')
    # 获取按照read_num从高到低排列的前三篇博客信息
    recommends = Topic.objects.all().order_by('read_num')[0:3]
    # 随机获取5篇博客
    topicfive = Topic.objects.all().values()
    results = random.sample(tuple(topicfive),5)
    # 随机获取3篇文章
    topicthrees = random.sample(tuple(topicfive),3)
    # 随机生成３篇文章
    titlethrees = random.sample(tuple(topicfive),3)
    # 判断是否有用户登录
    if 'id' and 'uname' in request.session:
        id = request.session['id']
        user = Users.objects.filter(id=id).values('uname')
        uname =user[0]['uname']
        return render(request,'index.html',locals())

# def search_views(request):
#     seek = request.GET.get('seek')
#     if not seek:
#         error_msg = '请输入关键词'
#         return render(request,'index.html',{'error_msg':error_msg})
#     topic_list = Topic.objects.filter(title__icontains=seek)
#     return render(request,'taglist.html',locals())

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
#             return render(request,'index.html',locals())
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
#                     resp = render(request,'index.html')
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
#
# def register_views(request):
#     if request.method == 'GET':
#         return render(request,'register.html')
#     else:
#         # 如果是post
#         uname = request.POST['uname']
#         users = Users.objects.filter(uname=uname)
#         if users:
#             # uname已存在
#             return render(request,'register.html',{'errMsg':'用户已存在'})
#         else:
#             # 如果不存在则取值保存到数据库
#             users = Users()
#             users.uname = request.POST['uname']
#             users.uemail = request.POST['uemail']
#             users.uurl = request.POST['uurl']
#             users.upwd = request.POST['upwd']
#             users.upwd = generate_password_hash(users.upwd)
#             # 保存会数据库
#             try:
#                 users.save()
#                 return redirect('/')
#             except Exception as ex:
#                 print(ex)
#                 return render(request,'register.html',{'errMsg':'请联系管理员'})
#
# def loginout_views(request):
#     url = request.META.get('HTTP_REFERER','/')
#     if 'id' in request.session and 'uname' in request.session:
#         del request.session['id']
#         del request.session['uname']
#         return redirect(url)




# def photo_views(request):
#     if 'uname' in request.session:
#         uname = request.session['uname']
#         user2 = Users.objects.filter(uname=uname).values('uname')
#         print(user2)
#         return render(request,'photo.html',locals())
#     else:
#         url = request.META.get('Referer','/')
#         return redirect(url)

# def time_views(request):
#     if 'uname' in request.session:
#         uname = request.session['uname']
#         user3 = Users.objects.filter(uname=uname).values('uname')
#         print(user3)
#         return render(request,'time.html',locals())
#     else:
#         url = request.META.get('Referer','/')
#         return redirect(url)

# def gbook_views(request):
#     if 'uname' in request.session:
#         uname = request.session['uname']
#         user4 = Users.objects.filter(uname=uname).values('uname')
#         print(user4)
#         return render(request,'gbook.html',locals())
#     else:
#         url = request.META.get('Referer','/')
#         return redirect(url)

# def about_views(request):
#     if 'uname' in request.session:
#         uname = request.session['uname']
#         user5 = Users.objects.filter(uname=uname).values('uname')
#         print(user5)
#         return render(request,'about.html',locals())
#     else:
#         url = request.META.get('Referer','/')
#         return redirect(url)

# def list_views(request):
#     if 'uname' in request.session:
#         uname = request.session['uname']
#         user7 = Users.objects.filter(uname=uname).values('uname')
#         print(user7)
#         return render(request, 'list.html', locals())
#     else:
#         url = request.META.get('Referer', '/')
#         return redirect(url)



# # 发表博客
# def release_views(request):
#     if request.method == 'GET':
#         # 判断是否有用户登录
#         if 'id' in request.session and 'uname' in request.session:
#             uname = request.session['uname']
#             user6 = Users.objects.filter(uname=uname).values('uname')
#             catename = Category.objects.all()
#             return render(request,'release.html',locals())
#         else:
#             return render(request,'login.html')
#     else:
#         # 创建Topic的对象topic
#         topic = Topic()
#         category = Category()
#         # 获取前端传过来的标题
#         topic.title = request.POST['author']
#         # 获取博客类型
#         topic.blogtype_id = request.POST['list']
#         category.cate_name = request.POST['category']
#         cate = Category.objects.filter(cate_name=category.cate_name).values('id')
#         # 判断标签是否存在
#         try:
#             if len(cate) == 0:
#                 Category.save(category)
#         except:
#             print('数据插入错误')
#         cate_id = Category.objects.filter(cate_name=category.cate_name).values('id')
#         topic.category_id = cate_id[0]['id']
#         # 获取id
#         topic.users_id = request.session['id']
#         # 获取文章内容
#         topic.content = request.POST['content']
#         # 获取发表时间
#         topic.pub_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         if request.FILES:
#             f = request.FILES.get('picture')
#             # 获取图片时间拓展名
#             ftime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#             # 获取.jpg
#             ext = f.name.split('.')[1]
#             # 重组图片名
#             filename = ftime+'.'+ext
#             topic.images = 'images/'+filename
#             # 上传路径
#             # 将文件以文件名进行保存
#             dir = ''.join(settings.STATICFILES_DIRS)
#             fname = dir + '/images/' + filename
#             with open(fname,'wb') as pic:
#                 for c in f.chunks():
#                     pic.write(c)
#         # 将数据保存会数据库
#         Topic.save(topic)
#         return redirect('/',locals())
#
# # 阅读记录
# def info_views(request):
#     # 获取文章id
#     topic_id = request.GET['id']
#     print(topic_id)
#     # 根据id查到对应文章
#     topic = Topic.objects.filter(id=topic_id).first()
#     print(topic)
#     # 更新阅读量
#     topic.read_num = topic.read_num + 1
#     topic.save()
#     # 查询上一篇，查询比当前博客id小的博客中的第一个
#     prevTop = Topic.objects.filter(id__lt=topic_id).order_by('-id').first()
#     prevTop_id = Topic.objects.filter(title=prevTop).values('id')
#     prevTopid = prevTop_id[0]['id']
#     # 查询下一篇，查询比当前博客id大的博客中的第一个
#     nextTop = Topic.objects.filter(id__gt=topic_id).first()
#     nextTop_id = Topic.objects.filter(title=nextTop).values('id')
#     nextTopid = nextTop_id[0]['id']
#     print(nextTopid)
#     return render(request,'info.html',locals())
#
# def pag_info_views(request):
#     # 获取文章id
#     topicid = request.GET['id']
#     # print(topicid)
#     topic = Topic.objects.filter(id=topicid).first()
#
#     nextTop = Topic.objects.filter(id=topicid).first()
#
#     return render(request,'info.html',locals())




















