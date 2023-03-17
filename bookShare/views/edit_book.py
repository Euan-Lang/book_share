from bookShare.forms import BookForm
from django.contrib.auth.models import User
from bookShare.models import Book
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url='bookShare:login')
def edit_book(request, book_id):
    book = Book.objects.get(book_id = book_id)
    if request.user.username != book.user_profile.user.username:
        return redirect(reverse('bookShare:browse')) #ensures only the user that listed the book can edit it.
    
    if request.method == 'POST':
        profile_form = BookForm(request.POST, instance=book)
        
        if profile_form.is_valid():
            
            if 'cover_image' in request.FILES:
                book.cover_image.delete(save=True)
                book.cover_image = request.FILES['user_image']
            else:
                profile_form.cover_image = book.cover_image

            profile_form.save()

            return redirect(reverse('bookShare:book_info', kwargs={'book_id':book_id}))
        else:
            print(profile_form.errors)

    else:
        profile_form = BookForm(
            {
                'title':book.title, 
                'publisher':book.publisher,
                'author':book.author,
                'isbn':book.isbn,
                'cover_image':book.cover_image,
                'genre':book.genre
            }
        )

    return render(request,'bookShare/edit_book.html')
