from django.shortcuts import render
from django.contrib.auth.models import User
from bookShare.models import UserProfile, Follows
from django.shortcuts import redirect
from django.urls import reverse
from bookShare.views.map_functions import *


def profile(request, user_id):
    context = {}

    user = User.objects.get(username=user_id)
    user_profile = UserProfile.objects.get(user=user)
    try:
        context = formatContextDict(getCoordsRequest(user_profile.post_code))
    except:
        context = {"invalid_map": True}
    context["profile"] = user_profile
    context["profile_attributes"] = {
        "location": {
            "label": "Location",
            "value": user_profile.location
        },
        "reputation": {
            "label": "Total Listing",
            "value": user_profile.reputation,
        },
        "joined": {
            "label": "Joined Date",
            "value": user_profile.joined_date,
        }
    }

    context["following"] = Follows.objects.filter(follower=user_profile)
    context["followers"] = Follows.objects.filter(following=user_profile)
    if request.user.is_authenticated and UserProfile.objects.filter(user=request.user).exists():
        context["is_following"] = context["followers"].filter(
            follower=UserProfile.objects.get(user=request.user)).exists()
    else:
        context["is_following"] = "invalid"

    return render(request, 'bookShare/profile.html', context=context)
