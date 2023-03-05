from django.db import models
from django.contrib.auth.models import User
import os


def rename(instance, file_name):
    extension = file_name.split('.')[-1]
    if instance.user.username:
        file_name = '{}.{}'.format(instance.user.username, extension)  
    
    return os.path.join('user/', file_name)

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=128)

class Publisher(models.Model):
    publisher_id = models.AutoField(primary_key=True)
    publisher_name = models.CharField(max_length=128)

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    location = models.CharField(max_length=128)
    post_code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=11)
    joined_date = models.DateField(auto_now_add=True)
    reputation = models.IntegerField()
    user_image = models.ImageField(upload_to=rename,null=True,blank=True)
    
    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username