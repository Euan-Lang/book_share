from django.shortcuts import render

def add_book(request):
    return render(request,'bookShare/add_book.html')
