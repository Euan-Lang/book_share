from bookShare.models import Interest, UserProfile, Book
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required(login_url="bookShare:login")
def remove_interest(request,book_id):
    if request.is_ajax and request.method == 'POST' and UserProfile.objects.filter(user = request.user).exists():
        book = Book.objects.get(book_id=book_id)
        user_profile = UserProfile.objects.get(user = request.user)
        if Interest.objects.filter(book = book,user_profile = user_profile).exists():
            Interest.objects.get(book = book,user_profile = user_profile).delete()

        return JsonResponse({}, status=200)

    return redirect(reverse('bookShare:book_info', kwargs={'book_id':book_id}))