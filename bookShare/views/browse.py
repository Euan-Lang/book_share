from django.shortcuts import render
from bookShare.models import Book
from django.db.models import Q

def browse(request):
    context = {}

    context["results"] = Book.objects.all() # By default, show all books

    if request.method == "POST": 
        query = request.POST["general_query"]
        context["results"] = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(isbn__icontains=query) | Q(genre__icontains=query) | Q(book_id__icontains=query) | Q(user_profile__user__username__icontains=query))
    
    return render(request,'bookShare/browse.html', context=context)
