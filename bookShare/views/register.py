import datetime
from bookShare.forms import UserForm, UserProfileForm
from django.shortcuts import render, redirect
from django.urls import reverse

DEFAULT_REPUTATION = 0

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('bookShare:browse')) # Already signed in.
    
    registered = False


    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.reputation = DEFAULT_REPUTATION
            profile.joined_date = datetime.date.today

            if 'user_image' in request.FILES:
                profile.user_image = request.FILES['user_image']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    
    return render(request,
        'bookShare/register.html',
        context = {'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered})