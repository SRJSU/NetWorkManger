from django.db import models

# Create your models here.

class User(models.Model):
    Username=models.CharField(max_length=24)
    UserPassword = models.CharField(max_length=30)
    UserEmail=models.EmailField(null=False)
    info=models.TextField(null=True)
    PhoneNum=models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.Username

class Tag(models.Model):
    tag_name=models.TextField(verbose_name='标签名',max_length=30)
    def __str__(self):
        return self.tag_name

class Article(models.Model):
    title = models.CharField(max_length=200)  # 博客标题
    date_time = models.DateField(auto_now_add=True)  # 博客日期
    content = models.TextField(blank=True, null=True)  # 文章正文
    author = models.ForeignKey(User, verbose_name=u'作者', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)  # 标签
    def __str__(self):
        return  self.title


