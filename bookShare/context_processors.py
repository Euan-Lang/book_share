from bookShare.models import UserProfile, Book


def base_processor(request):
    return_dict = {"left_nav_items": [
        {"name": "Browse", "url": "bookShare:browse"},
        {"name": "Search User", "url": "bookShare:user_search"},
        {"name": "Add Book", "url": "bookShare:add_book"},
    ], "right_nav_items": []}
    if request.user.is_authenticated:
        return_dict["right_nav_items"].append(
            {"name": "Logout", "url": "bookShare:logout"})

        # Check if associated UserProfile
        if UserProfile.objects.filter(user=request.user).exists():
            # Grab profile data so we can use it in base
            return_dict["profile"] = UserProfile.objects.get(user=request.user)
            # Add nav item with context to profile
            return_dict["right_nav_items"].append(
                {"name": "Profile",
                 "url": "bookShare:profile",
                 "context": request.user.username})

    else:
        return_dict["right_nav_items"].append(
            {"name": "Login", "url": "bookShare:login"})

    return_dict["latest_added_books"] = Book.objects.order_by(
        "-upload_time")[:3]

    return return_dict
