from django.shortcuts import render

def edit_book(request, genre, book_id):
    return render(request,'bookShare/edit_book.html')
