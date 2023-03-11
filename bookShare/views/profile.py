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

        context["following"] = Follows.objects.filter(follower = user_profile)
        context["followers"] = Follows.objects.filter(following=user_profile)
        if request.user.is_authenticated and UserProfile.objects.filter(user=request.user).exists():
            context["is_following"] = context["followers"].filter(follower=UserProfile.objects.get(user=request.user))
        else:
            context["is_following"] = "invalid"
    except:
        return redirect(reverse('bookShare:browse'))

    return render(request,'bookShare/profile.html', context=context)
