from django.shortcuts import render
from django.contrib.auth.models import User
from bookShare.models import Intrest, UserProfile, Book
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url="bookShare:login")
def add_intrest(request,book_id):
    book = Book.objects.get(book_id=book_id)
    if request.user.username != book.user_profile.user.username:
        user_profile = UserProfile.objects.get(request.user)
        if not Intrest.objects.filter(book_id=book_id,user_profile=user_profile).exists():
            Intrest.objects.create(book_id=book_id,user_profile=user_profile)
    
    return redirect(reverse('bookShare:book_info', kwargs={'book_id':book_id}))