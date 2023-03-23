from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect

def user_login(request):
    if request.user.is_authenticated:
        return redirect(reverse('bookShare:browse')) # Already signed in.
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('bookShare:browse'))
            else:
                return render(request, 'bookShare/login.html', context={"error_msg":"Your BookShare account is disabled."})
        else:
            print(f"Invalid login details: {username}, {password}")
            return render(request, 'bookShare/login.html', context={"error_msg":"Invalid login details supplied"})
    else:
        return render(request, 'bookShare/login.html')
