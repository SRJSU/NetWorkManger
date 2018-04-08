from django.urls import path,re_path
from Blog import views


urlpatterns = [
    path('', views.Index),
    re_path(r'articles/(?P<articlesid>[0-9]+)/',views.detail,name="detail")
]
