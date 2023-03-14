from django.shortcuts import render
from bookShare.models import Book
from django.shortcuts import redirect
from django.urls import reverse


def browse(request):
    context={}
    context['books'] = Book.objects.filter()
    return render(request,'bookShare/browse.html', context=context)
