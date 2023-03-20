from django.http import HttpResponse
from git import Repo # 
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        repo = Repo('./book_share')
        git = repo.git
        git.checkout('master')
        git.pull()
        return HttpResponse('pulled_success')
    return HttpResponse('get_request', status=400)