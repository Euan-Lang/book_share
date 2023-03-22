from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
import json

from bookShare.models import Book, UserProfile, Follows

from .map_functions import getCoordsRequest
from bookShare.utils.map_calculations import getLatLon


def browse(request):
    context = {}
    if request.method == "POST":
        general_query = request.POST["general_query"]
        checkbox_querys = json.loads(request.POST["checkbox_queries"])
        try:
            max_radius = int(request.POST["max_radius_query"])
        except ValueError:
            max_radius = 100_000_000  # Effectively infinity if no or incorrect input
        postcode = request.POST["postcode"]
        lat, lon = getLatLon(postcode)
        valid_postcode = lat != None
        available_only = True if request.POST["available_only"] == "true" else False
        following_only = True if request.POST["following_only"] == "true" else False
        mine_only = True if request.POST["mine_only"] == "true" else False
        reserved_for_me_only = True if request.POST["reserved_for_me_only"] == "true" else False
        sort_order = request.POST["sort"]

        # Select all books which contain the general query in any field
        results = Book.objects.filter(Q(title__icontains=general_query) | Q(author__icontains=general_query) | Q(isbn__icontains=general_query) | Q(
            genre__icontains=general_query) | Q(book_id__icontains=general_query) | Q(user_profile__user__username__icontains=general_query))
        
        # Filter books
        if "authors" in checkbox_querys:
            results = results.filter(author__in=checkbox_querys["authors"])
        if "publishers" in checkbox_querys:
            results = results.filter(
                publisher__in=checkbox_querys["publishers"])
        if "genres" in checkbox_querys:
            results = results.filter(genre__in=checkbox_querys["genres"])

        if available_only:
            results = results.filter(is_reserved__exact=False)

        if following_only:
            results = results.filter(user_profile__in=Follows.objects.filter(
                follower=UserProfile.objects.get(user=request.user)
            ).values_list("following"))

        if mine_only:
            results = results.filter(user_profile__user=request.user)

        if reserved_for_me_only:
            results = results.filter(reserved_user__user=request.user)
        
        if valid_postcode:
            ids = [book.book_id for book in results if book.user_profile.getDistance(
                lat, lon) <= max_radius]
            results = results.filter(book_id__in=ids)

        # Sort results into correct order
        context["results"] = sort_results(results, sort_order, lat, lon)
        
        return JsonResponse({"results_container": render(request, 'bookShare/browse_results.html', context=context).content.decode("utf-8"), "valid_postcode": valid_postcode})

    else:
        context["dropdowns"] = {
            "genres": Book.objects.values_list("genre").distinct(),
            "authors": Book.objects.values_list("author").distinct(),
            "publishers": Book.objects.values_list("publisher").distinct(),
        }
        if request.user.is_authenticated:
            context["user_postcode"] = UserProfile.objects.get(
                user=request.user).post_code
        return render(request, 'bookShare/browse.html', context=context)


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
    # Only sort by distance if a valid location is given
    elif (sort_order == "closest_first" or sort_order == "furthest_first") and user_lat != None:
        books = [book for book in query_set]
        books.sort(key=lambda book: book.user_profile.getDistance(
            user_lat, user_lon))
        if sort_order == "furthest_first":
            books.reverse()
        return books
    else:
        # Invalid sort input, so order alphabetically
        return query_set.order_by("title")
