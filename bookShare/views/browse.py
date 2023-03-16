from django.shortcuts import render
from bookShare.models import Book

def browse(request):
    context = {}

    context["results"] = Book.objects.filter() # By default, show all books

    if request.method == "POST": 
        query = request.POST["query_text"]
        context["results"] = Book.objects.filter()
    
    return render(request,'bookShare/browse.html', context=context)
