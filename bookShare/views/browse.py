from django.shortcuts import render
from bookShare.models import Book
from django.db.models import Q

def browse(request):
    context = {}
    print("ajax", request.is_ajax())
    if request.method == "POST":
        general_query = request.POST["general_query"]
        genre_query = request.POST["genre_query"]
        publisher_query = request.POST["publisher_query"]
        author_query = request.POST["author_query"]
        try:
            max_radius_query = int(request.POST["max_radius_query"])
        except ValueError:
            max_radius_query = 1000
        available_only = True if request.POST["available_only"] == "true" else False
        sort_order = request.POST["sort"]
        print(max_radius_query, available_only)
        
        # Select all books which contain the general query in any field
        results = Book.objects.filter(Q(title__icontains=general_query) | Q(author__icontains=general_query) | Q(isbn__icontains=general_query) | Q(genre__icontains=general_query) | Q(book_id__icontains=general_query) | Q(user_profile__user__username__icontains=general_query))
        # Filter to remove all books not containing the filter queries in their relevant fields
        results = results.filter(genre__icontains=genre_query)
        results = results.filter(publisher__icontains=publisher_query)
        results = results.filter(author__icontains=author_query)
        if available_only:
            results = results.filter(is_reserved__exact=False)
                
        # Sort results into correct order
        results = sort_results(results, sort_order)
        context["results"] = results
        return render(request,'bookShare/browse_results.html', context=context)
    else:
        return render(request,'bookShare/browse.html', context=context)

def sort_results(query_set, sort_order):
    orderings = {
        "az": "title",
        "za": "-title",
        # "closest_first": pass,
        # "furthest_first": ,
        "newest_first": "-upload_time",
        "oldest_first": "upload_time",
        "lowest_reputation_first": "user_profile__reputation",
        "highest_reputation_first": "-user_profile__reputation",
    }
    if orderings.get(sort_order):
        return query_set.order_by(orderings.get(sort_order))
    else:
        # Invalid sort input, so order alphabetically
        return query_set.order_by("title")