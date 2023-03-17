from django.shortcuts import render
from django.contrib.auth.models import User
from bookShare.models import Intrest, UserProfile, Book
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url="bookShare:login")
def remove_intrest(request,book_id):
    pass