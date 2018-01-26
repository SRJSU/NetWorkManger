from django.shortcuts import render, redirect
from django.http import HttpResponse
from NetWorkManage import models

# Create your views here.


def Login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        name=request.POST.get('Email')
        pwd=request.POST.get('Password')
        obj = models.User.objects.filter(UserEmail=name,UserPassword=pwd).first()
        if obj:
            print(obj)
            #1、生成随机字符串（sessionID）
            #2、通过cookie发送给客户端
            #3、服务端保存{zhanggen随机字符串:{'name':'zhanggen'.'email':'zhanggen@le.com'}}
            request.session['email']=obj.UserEmail #在Django 中一句话搞定
            return redirect('/index/')
        else:
            return render(request,'login.html',{'info':"用户名/密码错误"})

def Index(request):
    v = request.session.get('email')
    if v:
        return render(request, 'index.html', {'email': v})
    else:
        return redirect('/login/')