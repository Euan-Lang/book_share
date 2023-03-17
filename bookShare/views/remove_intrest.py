from bookShare.models import Intrest, UserProfile, Book
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url="bookShare:login")
def remove_intrest(request,book_id):
    if UserProfile.objects.filter(user = request.user).exists():
        book = Book.objects.get(book_id=book_id)
        user_profile = UserProfile.objects.get(user = request.user)
        if Intrest.objects.filter(book = book,user_profile = user_profile).exists():
            Intrest.objects.get(book = book,user_profile = user_profile).delete()

    return redirect(reverse('bookShare:book_info', kwargs={'book_id':book_id}))