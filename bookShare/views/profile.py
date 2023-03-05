from django.shortcuts import render

def profile(request, user_id):
    context = {"user_id":user_id}
    return render(request,'bookShare/profile.html', context=context)
