from django.shortcuts import render
from bookShare.models import Book
from django.shortcuts import redirect
from django.urls import reverse

def book_info(request, book_id):
    context={}

    book = Book.objects.get(book_id = book_id)
    context['book'] =book
    return render(request,'bookShare/book_info.html', context=context)
