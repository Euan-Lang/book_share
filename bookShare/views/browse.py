from django.db.models import Q
from django.db.models.functions import Sin, Cos, ACos
from django.http import JsonResponse
from django.shortcuts import render


from bookShare.models import Book

from bookShare.map_calculations import getLatLon

def browse(request):
    context = {}
    print("ajax", request.is_ajax())
    if request.method == "POST":
        # Read in data
        general_query = request.POST.get("general_query", "")
        genre_query = request.POST.get("genre_query", "")
        publisher_query = request.POST.get("publisher_query", "")
        author_query = request.POST.get("author_query", "")
        try:
            max_radius = int(request.POST.get("max_radius",""))
        except ValueError:
            max_radius = 100_000_000 # Effectively infinity if no or incorrect input
        lat, lon = getLatLon(request.POST.get("postcode", ""))
        valid_postcode = lat != None
        available_only = True if request.POST["available_only"] == "true" else False
        sort_order = request.POST.get("sort")
        
        # Select all books which contain the general query in any field
        results = Book.objects.filter(Q(title__icontains=general_query) | Q(author__icontains=general_query) | Q(isbn__icontains=general_query) | Q(genre__icontains=general_query) | Q(book_id__icontains=general_query) | Q(user_profile__user__username__icontains=general_query))
        
        # Filter to remove all books not containing the filter queries in their relevant fields
        results = results.filter(genre__icontains=genre_query)
        results = results.filter(publisher__icontains=publisher_query)
        results = results.filter(author__icontains=author_query)
        if available_only:
            results = results.filter(is_reserved__exact=False)
        
        # Handle Postcode filtering
        user_lat, user_lon = None, None
        if valid_postcode:
            ids = [book.book_id for book in results if book.user_profile.getDistance(lat, lon) <= max_radius]
            results = results.filter(book_id__in=ids)
        
        # Sort results into correct order
        context["results"] = sort_results(results, sort_order, lat, lon)
        return JsonResponse({"results_container":render(request,'bookShare/browse_results.html', context=context).content.decode("utf-8"), "valid_postcode": valid_postcode})
    else:
        return render(request,'bookShare/browse.html', context=context)

def sort_results(query_set, sort_order, user_lat, user_lon):
    orderings = {
        "az": "title",
        "za": "-title",
        "newest_first": "-upload_time",
        "oldest_first": "upload_time",
        "lowest_reputation_first": "user_profile__reputation",
        "highest_reputation_first": "-user_profile__reputation",
    }
    if orderings.get(sort_order):
        return query_set.order_by(orderings.get(sort_order))
    elif (sort_order == "closest_first" or sort_order == "furthest_first") and user_lat != None: # Only sort by distance if a valid location is given
        books = [book for book in query_set]
        books.sort(key=lambda book: book.user_profile.getDistance(user_lat, user_lon))
        if sort_order == "furthest_first":
            books.reverse()
        return books
    else:
        # Invalid sort input, so order alphabetically
        return query_set.order_by("title")