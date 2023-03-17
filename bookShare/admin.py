from django.contrib import admin
from bookShare.models import UserProfile, Book, Follows, Intrest

admin.site.register(UserProfile)
admin.site.register(Book)
admin.site.register(Follows)
admin.site.register(Intrest)