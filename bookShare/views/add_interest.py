from bookShare.models import Interest, UserProfile, Book
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required(login_url="bookShare:login")
def add_interest(request,book_id):
    book = Book.objects.get(book_id=book_id)
    if request.is_ajax and request.method == 'POST' and request.user.username != book.user_profile.user.username and UserProfile.objects.filter(user = request.user).exists():
        user_profile = UserProfile.objects.get(user = request.user)
        if not Interest.objects.filter(book_id=book_id,user_profile=user_profile).exists():
            Interest.objects.create(book_id=book_id,user_profile=user_profile)

        return JsonResponse({}, status=200)
    
    return redirect(reverse('bookShare:book_info', kwargs={'book_id':book_id}))