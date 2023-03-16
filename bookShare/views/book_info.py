from django.shortcuts import render
from bookShare.models import Book
from django.shortcuts import redirect
from django.urls import reverse

def book_info(request, book_id):
    context={}

    try:
        book = Book.objects.get(book_id = book_id)
        context['book'] = book
    except:
        return redirect(reverse('bookShare:browse'))
    
    return render(request,'bookShare/book_info.html', context=context)