from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('bookShare:browse'))
