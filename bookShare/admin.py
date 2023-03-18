from django.contrib import admin
from bookShare.models import UserProfile, Book, Follows, Interest

admin.site.register(UserProfile)
admin.site.register(Book)
admin.site.register(Follows)
admin.site.register(Interest)