from django.shortcuts import render
from django.contrib.auth.models import User
from bookShare.models import UserProfile
from django.http import JsonResponse

def user_search(request):
    context = {}

    if request.is_ajax and request.method == "POST": 
        username = request.POST.get("username", False)
        results = UserProfile.objects.filter(user__in=User.objects.filter(username__icontains=username))
        return JsonResponse({"instances":[result.user.username for result in results]}, status=200)


    return render(request,'bookShare/user_search.html')
