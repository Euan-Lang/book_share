from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=128)

class Publisher(models.Model):
    Publisher_id = models.AutoField(primary_key=True)
    Publisher_name = models.CharField(max_length=128)

class UserProflie(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    display_name = models.CharField(max_length=64)
    location = models.CharField(max_length=128)
    post_code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=11)
    joined_date = models.DateField()
    reputation = models.IntegerField()
    user_image = models.CharField(max_length=64)