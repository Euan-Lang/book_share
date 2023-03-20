from django.test import TestCase
from bookShare.models import Book, UserProfile
from django.contrib.auth.models import User
from django.urls import reverse

def add_user(username, email, password):
    newUser = User()
    newUser.username = username
    newUser.email = email
    newUser.password = password
    newUser.save()

    return newUser

def add_user_profile(user, location, post_code):
    newProfile = UserProfile()
    newProfile.user = user
    newProfile.location = location
    newProfile.post_code = post_code
    newProfile.reputation = 0
    newProfile.save()

    return newProfile

def add_book(profile, title, publisher, author, genre):
    newBook = Book()
    newBook.user_profile = profile
    newBook.title = title
    newBook.publisher = publisher
    newBook.author = author
    newBook.genre = genre
    newBook.save()

    return newBook

class UserTests(TestCase):
    def test_new_user_is_registered(self):
        user = add_user("Bob", "123@gmail.com", "testPassword")
        profile = add_user_profile(user, "Exampleville", "XXXXXX")
        self.assertTrue(UserProfile.objects.filter(user=User.objects.get(username="Bob")).exists())

class BookTests(TestCase):

    def test_new_book_exists(self):
        """Create a new book and check it has been correctly saved."""
        user = add_user("Bob", "123@gmail.com", "testPassword")
        profile = add_user_profile(user, "Exampleville", "XXXXXX")
        add_book(profile, "How to Test?", "Test Publisher", "Mr. Test", "Test Genre")

        self.assertEqual(len(Book.objects.all()), 1)

