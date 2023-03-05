from django.contrib import admin
from bookShare.models import UserProfile, Author, Publisher, Book

admin.site.register(UserProfile)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)