from django.http import HttpResponse
from git import Repo # 
from django.views.decorators.csrf import csrf_exempt
import subprocess

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        repo = Repo('./book_share')
        git = repo.git
        git.checkout('main')
        git.pull()
        bashCommand = "touch /var/www/euanlang28_pythonanywhere_com_wsgi.py"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        return HttpResponse('pulled_success')
    return HttpResponse('get_request', status=400)