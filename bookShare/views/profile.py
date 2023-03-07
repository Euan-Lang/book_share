from django.shortcuts import render
from django.contrib.auth.models import User
from bookShare.models import UserProfile, Follows
from django.shortcuts import redirect
from django.urls import reverse

def profile(request, user_id):
    context = {}

    try:
        user = User.objects.get(username = user_id)
        user_profile = UserProfile.objects.get(user = user)
        context["profile"] = user_profile

        following = Follows.objects.filter(follower = user_profile)
        context["following"] = following

    except :
        return redirect(reverse('bookShare:browse'))

    return render(request,'bookShare/profile.html', context=context)
