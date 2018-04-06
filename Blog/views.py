from django.shortcuts import render, redirect
from Blog.models import User,Article,Tag




def Index(request):
    articles=Article.objects.all()
    tag_list=Tag.objects.all()
    return render(request, 'index.html',{"artical_list": articles,
                                         "tag_list":tag_list})
