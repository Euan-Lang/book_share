from django.shortcuts import render
from django.contrib.auth.models import User
from bookShare.models import UserProfile
from django.shortcuts import redirect
from django.urls import reverse

def user_search(request):
    context = {}

    if request.method == "POST": 
        username = request.POST["username"]
        if not username == "":
            context["results"] = UserProfile.objects.filter(user__in=User.objects.filter(username__icontains=username))


    return render(request,'bookShare/user_search.html', context=context)
