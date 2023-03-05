from django.contrib import admin
from bookShare.models import UserProfile, Author, Publisher

admin.site.register(UserProfile)
admin.site.register(Author)
admin.site.register(Publisher)