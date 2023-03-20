from bookShare.models import Interest, UserProfile, Book, User
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url="bookShare:login")
def accept_interest(request, book_id, reserved_user_id):
    book = Book.objects.get(book_id=book_id)
    if UserProfile.objects.filter(user=request.user).exists() and book.user_profile == UserProfile.objects.get(user = request.user):
        if book.is_reserved == False:
            book.is_reserved = True;
            book.reserved_user = UserProfile.objects.get(user=User.objects.get(username=reserved_user_id))
        else:
            book.is_reserved = False;
            book.reserved_user = None;
        book.save()


    return redirect(reverse('bookShare:book_info', kwargs={'book_id':book_id}))