from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from NetWorkManage import models


# Create your views here.
from NetWorkManage.forms import UserModelForm


def Login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        objFrom = UserModelForm(request.POST)
        if objFrom.is_valid():
            name = objFrom.clean().get('UserEmail')
            pwd = objFrom.clean().get('UserPassword')
            obj = models.User.objects.filter(UserEmail=name, UserPassword=pwd).first()
            if obj:
            # 1、生成随机字符串（sessionID）
            # 2、通过cookie发送给客户端
            # 3、服务端保存{zhanggen随机字符串:{'name':'zhanggen'.'email':'zhanggen@le.com'}}
                request.session['email'] = obj.UserEmail  # 在Django 中一句话搞定
                return redirect('/index/')
            else:
                return render(request, 'login.html', {'info': "用户名/密码错误"})
        else:
            return render(request, 'login.html', {'info': "用户名/密码格式错误"})


def Index(request):
    v = request.session.get('email')
    # vv=Session.objects.get(pk='ku3im28nmzqfimwevwhmhfi4970fc2qo')
    # print(vv.get_decoded())
    if v:
        return render(request, 'index.html', {'email': v})
    else:
        return redirect('/login/')


def LogOut(request):
    v = request.session.get('email')
    if v:
        print(v+"退出")
        try:
            del request.session['email']
        except:
            print("删除session错误")
        return redirect('/login/')
