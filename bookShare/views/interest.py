from bookShare.models import Interest, UserProfile, Book
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url='bookShare:login')
def interested(request,book_id):
    book = Book.objects.get(book_id=book_id)
    if request.user.username == book.user_profile.user.username:
        context = {}
        results = Interest.objects.filter(book=book)
        context['results'] = [interest.user_profile for interest in results]
        context['interested'] = str(len(context['results']))
        return render(request,'bookShare/interest.html', context=context)
    else:
        return redirect(reverse('bookShare:book_info', kwargs={'book_id':book.book_id}))