from django.shortcuts import render
from django.contrib.auth.models import User
from bookShare.models import Follows, UserProfile
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def follow(request, user_id):
    if request.user.username != user_id:
        other_user = UserProfile.objects.get(user=User.objects.get(username=user_id))
        profile = UserProfile.objects.get(user=request.user)

        if not Follows.objects.filter(follower=profile, following=other_user).exists():
            Follows.objects.create(follower=profile, following=other_user)

    return redirect(reverse('bookShare:profile', kwargs={'user_id':user_id}))
