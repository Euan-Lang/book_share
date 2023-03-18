from django.shortcuts import render
from django.contrib.auth.models import User
from bookShare.models import Follows, UserProfile
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def unfollow(request, user_id):
    if request.is_ajax and request.method == "POST" and request.user.username != user_id:
        other_user = UserProfile.objects.get(user=User.objects.get(username=user_id))
        profile = UserProfile.objects.get(user=request.user)

        if Follows.objects.filter(follower=profile, following=other_user).exists():
            Follows.objects.get(follower=profile, following=other_user).delete()
            
        return JsonResponse({"follow_count":len(Follows.objects.filter(following=other_user))}, status=200)

    return redirect(reverse('bookShare:profile', kwargs={'user_id':user_id}))
