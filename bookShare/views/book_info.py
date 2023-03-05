from django.shortcuts import render

def book_info(request, genre, book_id):
    return render(request,'bookShare/book_info.html')
