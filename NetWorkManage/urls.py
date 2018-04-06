from django.urls import path
from NetWorkManage import views


urlpatterns = [
    path('', views.Index),
]