
from bookShare.forms import UserProfileForm
from django.contrib.auth.models import User
from bookShare.models import UserProfile
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url='bookShare:login')
def edit_profile(request, user_id):
    if request.user.username != user_id:
        return redirect(reverse('bookShare:browse')) # Not valid user

    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':

        profile_form = UserProfileForm(request.POST, instance=profile)

        if profile_form.is_valid():
            

            if 'user_image' in request.FILES:
                profile.user_image.delete(save=True)
                profile.user_image = request.FILES['user_image']
            else:
                profile_form.user_image = profile.user_image

            profile_form.save()

            return redirect(reverse('bookShare:profile', kwargs={'user_id':user_id}))
        else:
            print(profile_form.errors)
    else:
        profile_form = UserProfileForm(instance=profile)

    
    return render(request,
        'bookShare/edit_profile.html',
        context = {
        'profile_form': profile_form,
        'user_id':user_id,
        'location':profile.location,
        'post_code':profile.post_code,
        'phone_number':profile.phone_number,
        })