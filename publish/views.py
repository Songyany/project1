from django.shortcuts import render,redirect
from index.models import *
from project1 import settings
import datetime

# Create your views here.
# 发表博客
def release_views(request):
    if request.method == 'GET':
        # 判断是否有用户登录
        if 'id' in request.session and 'uname' in request.session:
            uname = request.session['uname']
            user = Users.objects.filter(uname=uname).values('uname')
            uname = user[0]['uname']
            catename = Category.objects.all()
            return render(request,'release.html',locals())
        else:
            return render(request,'login.html')
    else:
        # 创建Topic的对象topic
        topic = Topic()
        category = Category()
        # 获取前端传过来的标题
        topic.title = request.POST['author']
        # 获取博客类型
        topic.blogtype_id = request.POST['list']
        category.cate_name = request.POST['category']
        cate = Category.objects.filter(cate_name=category.cate_name).values('id')
        # 判断标签是否存在
        try:
            if len(cate) == 0:
                Category.save(category)
        except:
            print('数据插入错误')
        cate_id = Category.objects.filter(cate_name=category.cate_name).values('id')
        topic.category_id = cate_id[0]['id']
        # 获取id
        topic.users_id = request.session['id']
        # 获取文章内容
        topic.content = request.POST['content']
        # 获取发表时间
        topic.pub_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if request.FILES:
            f = request.FILES.get('picture')
            # 获取图片时间拓展名
            ftime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            # 获取.jpg
            ext = f.name.split('.')[1]
            # 重组图片名
            filename = ftime+'.'+ext
            topic.images = 'images/'+filename
            # 上传路径
            # 将文件以文件名进行保存
            dir = ''.join(settings.STATICFILES_DIRS)
            fname = dir + '/images/' + filename
            with open(fname,'wb') as pic:
                for c in f.chunks():
                    pic.write(c)
        # 将数据保存会数据库
        Topic.save(topic)
        return redirect('/',locals())

# 阅读记录
def info_views(request):
    # 获取文章id
    topic_id = request.GET['id']
    print(topic_id)
    # 根据id查到对应文章
    topic = Topic.objects.filter(id=topic_id).first()
    print(topic)
    # 更新阅读量
    topic.read_num = topic.read_num + 1
    topic.save()
    # 查询上一篇，查询比当前博客id小的博客中的第一个
    prevTop = Topic.objects.filter(id__lt=topic_id).order_by('-id').first()
    prevTop_id = Topic.objects.filter(title=prevTop).values('id')
    # prevTopid = prevTop_id[0]['id']
    # 查询下一篇，查询比当前博客id大的博客中的第一个
    nextTop = Topic.objects.filter(id__gt=topic_id).first()
    nextTop_id = Topic.objects.filter(title=nextTop).values('id')
    # nextTopid = nextTop_id[0]['id']
    # print(nextTopid)
    return render(request,'info.html',locals())

def pag_info_views(request):
    # 获取文章id
    topicid = request.GET['id']
    # print(topicid)
    topic = Topic.objects.filter(id=topicid).first()

    nextTop = Topic.objects.filter(id=topicid).first()

    return render(request,'info.html',locals())