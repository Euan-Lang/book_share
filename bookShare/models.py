from django.db import models
from django.contrib.auth.models import User
import os


def renameUser(instance, file_name):
    extension = file_name.split('.')[-1]
    if instance.user.username:
        file_name = '{}.{}'.format(instance.user.username, extension)  
    
    return os.path.join('user/', file_name)

def renameBook(instance, file_name):
    extension = file_name.split('.')[-1]
    if instance.book_id:
        file_name = '{}.{}'.format(instance.book_id, extension)  
    
    return os.path.join('book/', file_name)

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
    user_image = models.ImageField(upload_to=renameUser,null=True,blank=True)
    follows = models.ManyToManyField("self",blank=True)
    
    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username
    
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    user_profile = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    publisher_id = models.ManyToManyField(Publisher)
    isbn = models.IntegerField()
    cover_image = models.ImageField(upload_to=renameBook,null=True,blank=True)
    title = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
    upload_time = models.DateTimeField(auto_now_add= True)
    is_reserved = models.BooleanField(default=False)