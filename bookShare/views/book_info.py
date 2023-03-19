from django.shortcuts import render
from bookShare.views.map_functions import getCoordsContextDict
def book_info(request, genre, book_id):



    return render(request,'bookShare/book_info.html')



