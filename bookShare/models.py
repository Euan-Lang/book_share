from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4
from django.core.validators import FileExtensionValidator



def rename_user(instance, file_name):
    extension = file_name.split('.')[-1]
    if instance.user.username:
        file_name = '{}.{}'.format(instance.user.username, extension)

    return os.path.join('user/', file_name)


def rename_book(instance, file_name):
    extension = file_name.split('.')[-1]
    file_name = '{}.{}'.format(uuid4().hex, extension)

    return os.path.join('book/', file_name)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=128)
    post_code = models.CharField(max_length=7)
    phone_number = models.CharField(max_length=11, null = True, blank = True)
    joined_date = models.DateField(auto_now_add=True)
    reputation = models.IntegerField()
    user_image = models.ImageField(
        upload_to=rename_user, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Follows(models.Model):
    follow_id = models.AutoField(primary_key=True)
    follower = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.CASCADE, related_name="following")

    def __str__(self):
        return self.follower.user.username + " -> " + self.following.user.username


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    isbn = models.IntegerField(null=True)
    cover_image = models.ImageField(
        upload_to=rename_book, null=True, blank=True)
    title = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
    upload_time = models.DateTimeField(auto_now_add=True)
    is_reserved = models.BooleanField(default=False)
    reserved_user = models.ForeignKey(UserProfile, null=True, blank=True,on_delete=models.SET_NULL,related_name="reserved_user")

    def __str__(self):
        return str(self.book_id)+" - " + self.title
    
class Interest(models.Model):
    interest_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_profile)+ " is interested in "+ str(self.book_id)

