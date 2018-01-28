from django.db import models

# Create your models here.

class User(models.Model):
    UserEmail=models.EmailField(unique=True)
    UserPassword=models.CharField(max_length=30)
    def __unicode__(self):
        return self.UserEmail



class UserInfo(models.Model):
    id=models.ForeignKey('User',on_delete=models.CASCADE,primary_key=True)
    info=models.TextField()
    PhoneNum=models.CharField(max_length=30)
    def __unicode__(self):
        return self.info



class SSHHost(models.Model):
    Host=models.CharField(max_length=15)
    PWD=models.CharField(max_length=50)
    def __unicode__(self):
        return self.Host

