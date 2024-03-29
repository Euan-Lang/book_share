import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from bookShare.forms import BookForm
from bookShare.models import Book, UserProfile
from django.urls import reverse

@login_required(login_url="bookShare:login")
def add_book(request):
    added = False
    submitted = False
    context = {}
    if request.method == 'POST':
        

        book_form = BookForm(request.POST)
        if book_form.is_valid():
            user = request.user
            user_profile = UserProfile.objects.get(user = user)
            user_profile.reputation += 1;
            user_profile.save()
            book = book_form.save(commit=False)
            book.user_profile = user_profile
            if "cover_image" in request.FILES:
                book.cover_image = request.FILES['cover_image']
            book.upload_time = datetime.datetime.now
            book.is_reserved = False
            book.save()
            return redirect(reverse("bookShare:book_info", kwargs={'book_id':book.book_id}))            
        else:
            context["errors"] = book_form.errors
        
        submitted =True
        
    else:
        book_form = BookForm()

    context['book_form'] = book_form
    context["added"] = added
    context["submitted"] = submitted

    
    return render(request,'bookShare/add_book.html', context=context)
