from django.db import models

# Create your models here.

class User(models.Model):
    UserEmail=models.EmailField(unique=True)
    UserPassword=models.CharField(max_length=30)
    def __unicode__(self):
        return self.UserEmail


class UserInfo(models.Model):
    User=models.ForeignKey('User',on_delete=models.CASCADE)
    info=models.TextField()
    PhoneNum=models.CharField(max_length=30)
    def __unicode__(self):
        return self.info