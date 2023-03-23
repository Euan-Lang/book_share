from django.shortcuts import render
from bookShare.models import Book, UserProfile, Interest
from django.shortcuts import redirect
from django.urls import reverse
from bookShare.views.map_functions import getCoordsContextDict


def book_info(request, book_id):
    try:
        context = getCoordsContextDict(book_id)
    except:
        context = {"invalid_map": True}
    try:
        book = Book.objects.get(book_id=book_id)
    except:
        return redirect(reverse("bookShare:browse"))
    context['book'] = book
    if book.is_reserved:
        context["interested_users"] = Interest.objects.filter(book_id=book_id).filter(
            user_profile__user__username=book.reserved_user.user.username)
    else:
        context["interested_users"] = Interest.objects.filter(book_id=book_id)
    if request.user.is_authenticated and UserProfile.objects.filter(user=request.user).exists():
        user_profile = UserProfile.objects.get(user=request.user)
        context['interested'] = Interest.objects.filter(
            book_id=book_id, user_profile=user_profile).exists()
        context['user_books'] = Book.objects.filter(
            user_profile__user__username=book.user_profile.user.username).count()
    else:
        context['interested'] = 'invalid'

    return render(request, 'bookShare/book_info.html', context=context)
