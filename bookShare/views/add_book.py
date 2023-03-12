import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bookShare.forms import BookForm
from bookShare.models import Book, UserProfile

@login_required
def add_book(request):
    added = False
    if request.method == 'POST':
        

        book_form = BookForm(request.POST)
        if book_form.is_valid():
            user = request.user
            user_profile = UserProfile.objects.filter(user = user)
            book = book_form.save(commit=False)
            book.user_profile = user_profile
            if "cover_image" in request.FILES:
                book.cover_image = request.Files['cover_image']
            book.upload_time = datetime.datetime.utcnow
            book.is_reserved = False
            book.save()
            added =True
        else:
            print(book_form.errors)

    else:
        book_form = BookForm()
    
    return render(request,'bookShare/add_book.html', context={'book_form': book_form,'added':added})
