from django.test import TestCase
from bookShare.models import Book, UserProfile
from django.contrib.auth.models import User
from django.urls import reverse
from django.middleware.csrf import get_token

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

def create_bob():
    user = add_user("Bob", "123@gmail.com", "testPassword")
    profile = add_user_profile(user, "Exampleville", "XXXXXX")

    return profile

class UserTests(TestCase):
    def test_new_user_is_registered(self):
        """Test a new user gets added to the database"""
        create_bob()
        self.assertTrue(UserProfile.objects.filter(user=User.objects.get(username="Bob")).exists())

    def test_user_search_json(self):
        """Check post request returns correct table"""
        create_bob()
        data = {
            "username":"bo",
            "csrfmiddlewaretoken":""
        }
        res = self.client.post(reverse("bookShare:user_search"), data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue("Bob" in res.content.decode())

    def test_profile_displays_information(self):
        profile = create_bob()
        profile.reputation = 3
        profile.save()
        response = self.client.get("/bookShare/Bob/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bob")
        self.assertContains(response, "Exampleville")
        self.assertContains(response, "3")

class BookTests(TestCase):

    def test_new_book_exists(self):
        """Create a new book and check it has been correctly saved."""
        profile = create_bob()
        add_book(profile, "How to Test?", "Test Publisher", "Mr. Test", "Test Genre")

        self.assertEqual(len(Book.objects.all()), 1)

    def test_browse_view(self):
        """ Check both books are displayed correctly in browse page """
        profile = create_bob()
        add_book(profile, "How to Test", "Test Publisher", "Mr. Test", "Test Genre")
        add_book(profile, "How to Check", "Test Publisher", "Mr. Test", "Test Genre")

        response = self.client.get(reverse("bookShare:browse"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "How to Test")
        self.assertContains(response, "How to Check")


