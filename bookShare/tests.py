from django.test import TestCase
from bookShare.models import Book, UserProfile, Interest, Follows
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.hashers import make_password

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
    user = add_user("Bob", "123@gmail.com", make_password("testPassword"))
    profile = add_user_profile(user, "Exampleville", "XXXXXX")

    return profile

def create_john():
    user = add_user("John", "321@gmail.com", make_password("testPassword"))
    profile = add_user_profile(user, "Exampleville", "XXXXXX")

    return profile

def create_dave():
    user = add_user("Dave", "213@gmail.com", make_password("testPassword"))
    profile = add_user_profile(user, "Exampleville", "XXXXXX")

    return profile
    

class UserTests(TestCase):
    def test_new_user_is_registered(self):
        """Test a new user gets added to the database"""
        create_bob()
        self.assertTrue(UserProfile.objects.filter(user=User.objects.get(username="Bob")).exists())

    def test_user_gets_redirected(self):
        """Test a user gets redirected to login when attempting to add book"""
        response = self.client.get(reverse("bookShare:add_book"))
        self.assertEqual(response.status_code, 302) # Redirect

        response = self.client.get(reverse("bookShare:add_book"), follow=True)
        self.assertEqual(response.status_code, 200) # Follows through to login page
        self.assertContains(response, "Login")

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
        """Check profile displays data correctly"""
        profile = create_bob()
        profile.reputation = 3
        profile.save()
        response = self.client.get(reverse("bookShare:profile", kwargs={"user_id":"Bob"}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bob")
        self.assertContains(response, "Exampleville")
        self.assertContains(response, "3")

    def test_user_login(self):
        """Check user can successfully log in"""
        create_bob()
        login = self.client.login(username="Bob",password="testPassword")
        self.assertTrue(login)

    def test_profile_displays_edit(self):
        """Check profile displays edit button to owner"""
        create_bob()
        self.client.login(username="Bob",password="testPassword")

        response = self.client.get(reverse("bookShare:profile", kwargs={"user_id":"Bob"}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Edit")

    def test_check_follow(self):
        """ Check follow object is created when John follows Bob """
        bob = create_bob()
        john = create_john()
        self.client.login(username="John",password="testPassword")
        data = {
            "csrfmiddlewaretoken":""
        }
        response = self.client.post(reverse("bookShare:follow", kwargs={"user_id":"Bob"}), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Follows.objects.all()), 1)
        self.assertTrue(Follows.objects.all()[0].follower == john)
        self.assertTrue(Follows.objects.all()[0].following == bob)

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

    def test_book_info_information(self):
        """ Check book info displayed correctly on page """
        profile = create_bob()
        book = add_book(profile, "How to Test", "Test Publisher", "Mr. Test", "Test Genre")
        response = self.client.get(reverse("bookShare:book_info", kwargs={"book_id":book.book_id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "How to Test")
        self.assertContains(response, "Test Publisher")
        self.assertContains(response, "Mr. Test")
        self.assertContains(response, "Test Genre")

    def test_logged_in_user_sees_edit(self):
        """ Check logged in user sees owner-only buttons """
        profile = create_bob()
        book = add_book(profile, "How to Test", "Test Publisher", "Mr. Test", "Test Genre")
        self.client.login(username="Bob",password="testPassword")
        
        response = self.client.get(reverse("bookShare:book_info", kwargs={"book_id":book.book_id}))
        self.assertEqual(response.status_code, 200)
        
        self.assertContains(response, "Edit")
        self.assertContains(response, "View Interested Users")

    def test_check_register_interest(self):
        """Check interest is registered when John registers interest on Bob's book"""
        bob = create_bob()
        book = add_book(bob, "How to Test", "Test Publisher", "Mr. Test", "Test Genre")
        john = create_john()
        self.client.login(username="John",password="testPassword")
        data = {
            "csrfmiddlewaretoken":""
        }
        response = self.client.post(reverse("bookShare:add_interest", kwargs={"book_id":book.book_id}), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Interest.objects.all()), 1)
        self.assertTrue(Interest.objects.all()[0].book == book)
        self.assertTrue(Interest.objects.all()[0].user_profile == john)

    def test_check_reserved(self):
        """Check correct reserved details show up when reserved for John"""
        bob = create_bob()
        book = add_book(bob, "How to Test", "Test Publisher", "Mr. Test", "Test Genre")
        john = create_john()
        book.is_reserved = True
        book.reserved_user = john
        book.save()
        self.client.login(username="John",password="testPassword")
       
        response = self.client.get(reverse("bookShare:book_info", kwargs={"book_id":book.book_id}))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Register Interest")
        self.assertContains(response, "Reserved for you")

    def test_check_cant_register_interest(self):
        """Check Dave can't register interest if reserved for John"""
        bob = create_bob()
        book = add_book(bob, "How to Test", "Test Publisher", "Mr. Test", "Test Genre")
        john = create_john()
        book.is_reserved = True
        book.reserved_user = john
        book.save()
        create_dave()
        self.client.login(username="Dave",password="testPassword")
       
        response = self.client.get(reverse("bookShare:book_info", kwargs={"book_id":book.book_id}))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Register Interest")