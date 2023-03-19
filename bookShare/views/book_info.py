from django.shortcuts import render
from bookShare.models import Book, UserProfile, Interest
from django.shortcuts import redirect
from django.urls import reverse

def book_info(request, book_id):
    context={}

    try:
        book = Book.objects.get(book_id = book_id)
        context['book'] = book
        if request.user.is_authenticated and UserProfile.objects.filter(user=request.user).exists():
            user_profile = UserProfile.objects.get(user = request.user)
            context['interested'] = Interest.objects.filter(book_id = book_id,user_profile=user_profile).exists()
        else:
            context['interested'] = 'invalid'
    except:
        return redirect(reverse('bookShare:browse'))
    
    return render(request,'bookShare/book_info.html', context=context)