from bookShare.models import UserProfile

def base_processor(request):
    return_dict = {"nav_items":[
        {"name":"Browse", "url":"bookShare:browse"},
        {"name":"Search User", "url":"bookShare:user_search"}
    ]}
    if request.user.is_authenticated:
        return_dict["nav_items"].append({"name":"Logout", "url":"bookShare:logout"})

        if UserProfile.objects.filter(user=request.user).exists(): # Check if associated UserProfile 
            # Grab profile data so we can use it in base
            return_dict["profile"] = UserProfile.objects.get(user=request.user) 
            # Add nav item with context to profile
            return_dict["nav_items"].append(
                {"name":"Profile",
                 "url": "bookShare:profile",
                 "context": request.user.username})

    else:
        return_dict["nav_items"].append({"name":"Login", "url":"bookShare:login"})

    return return_dict