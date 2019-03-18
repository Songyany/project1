# coding: utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Users(models.Model):
    uname = models.CharField(max_length=30,null=False,verbose_name='用户名')
    uemail = models.EmailField(verbose_name='邮箱')
    uurl = models.CharField(max_length=100,null=False,verbose_name='个人主站网址')
    upwd = models.CharField(max_length=200,null=False)
    isActive = models.BooleanField(default=False,verbose_name='是否是作者')

    def __str__(self):
        return self.uname

    class Meta:
        db_table = 'users'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

class Category(models.Model):
    cate_name = models.CharField(max_length=20,null=False,verbose_name='分类名称')

    def __str__(self):
        return self.cate_name

    class Meta:
        db_table = 'category'
        verbose_name = '分类名称'
        verbose_name_plural = verbose_name

class BlogType(models.Model):
    type_name = models.CharField(max_length=20,null=False,verbose_name='类型名称')
    def __str__(self):
        return self.type_name
    class Meta:
        db_table = 'blogtype'
        verbose_name = '博客类型'
        verbose_name_plural = verbose_name


class Topic(models.Model):
    title = models.CharField(max_length=200,null=False,verbose_name='标题')
    pub_date = models.DateField(auto_now=True,null=False,verbose_name='发表时间')
    read_num = models.IntegerField(null=True,verbose_name='阅读量',default=0)
    content = models.TextField(verbose_name='内容')
    images = models.ImageField(upload_to='static/images',default=None,verbose_name='图片',null=True)
    # 关联blogtype
    blogtype = models.ForeignKey('BlogType',on_delete=models.CASCADE)
    # 关联category
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    # Users与Topic的多对多关系
    users = models.ForeignKey('Users',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'topic'
        verbose_name = '博客信息'
        verbose_name_plural = verbose_name

    def profile(self):
        if len(str(self.content))>10:
            return '{}...'.format(str(self.content)[0:10])
        else:
            return str(self.content)
    profile.allow_tags = True



class Reply(models.Model):
    content = models.TextField(verbose_name='评论内容')
    reply_time = models.DateField(auto_now=True,verbose_name='评论时间')
    # 关联Users
    users = models.ForeignKey('Users',on_delete=models.CASCADE)
    # 关联topic
    topic = models.ForeignKey('Topic',on_delete=models.CASCADE)

    class Meta:
        db_table = 'reply'
        verbose_name = '回复内容'
        verbose_name_plural = verbose_name

class Voke(models.Model):
    # 关联Users
    users = models.ForeignKey('Users',on_delete=models.CASCADE)
    # 关联topicer
    topic = models.ForeignKey('Topic',on_delete=models.CASCADE)

    class Meta:
        db_table = 'voke'
        verbose_name = '点赞详情'
        verbose_name_plural = verbose_name

