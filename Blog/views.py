from django.shortcuts import render, redirect, get_object_or_404
from Blog.models import User,Article,Tag
import markdown



def Index(request):
    articles=Article.objects.all()
    tag_list=Tag.objects.all()
    return render(request, 'index.html',{"artical_list": articles,
                                         "tag_list":tag_list})


def detail(request,articlesid):
    artical=get_object_or_404(Article, id=articlesid)
    artical.content = markdown.markdown(artical.content,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'detail.html', context={'artical':artical})
