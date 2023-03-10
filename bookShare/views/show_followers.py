from django.shortcuts import render
from django.contrib.auth.models import User
from bookShare.models import UserProfile, Follows
from django.shortcuts import redirect
from django.urls import reverse

def show_followers(request, user_id):
    context = {}
    results = Follows.objects.filter(
        following__in = UserProfile.objects.filter(
            user=User.objects.get(username=user_id)
            )
        )
    context["results"] = [follow.follower for follow in results]
    context["display_name"] = "Followers (" + str(len(context["results"])) + ")"


    return render(request,'bookShare/show_users.html', context=context)

def show_following(request, user_id):
    context = {}
    results = Follows.objects.filter(
        follower__in = UserProfile.objects.filter(
            user=User.objects.get(username=user_id)
            )
        )
    context["results"] = [follow.following for follow in results]
    context["display_name"] = "Following (" + str(len(context["results"])) + ")"


    return render(request,'bookShare/show_users.html', context=context)
