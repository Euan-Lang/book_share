import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','book_share.settings')
import django
django.setup()

from bookShare.models import UserProfile,User,Follows,Book

def populate():
    #add user data here
    user_data=[
            {"user_name":"testuser1",
            "password":"hello123456789",
            "location":"Hamilton",
            "post_code":"ML38LT",
            "phone":"07986851525",
            "reputation":0,
            },
            {
            "user_name":"testuser2",
            "password":"hello123456789",
            "location":"Hamilton",
            "post_code":"ML36PZ",
            "phone":"01698365241",
            "reputation":0,
            }
        ]
    #add book data here
    book_data=[
        {"user_name":"testuser1",
         "publisher":"MnM Publishing",
         "author":"john williamson",
         "isbn":"2463472534658",
         "title":"CS1P - Introduction",
         "genre":"computing science"
        }
    ]


    def add_user(user_name,password,location,post_code,phone,reputation):
        user = User.objects.get_or_create(username=user_name, password=password)[0]
        userProfile = UserProfile.objects.get_or_create(user=user,location=location,post_code=post_code,reputation=reputation,phone_number=phone)[0]
        userProfile.save()

    def add_book(user,publisher,author,isbn,title,genre):
        book = Book.objects.get_or_create(user_profile = user,publisher=publisher,author=author,isbn=isbn,title=title,genre=genre)[0]
        book.save()
        
    def follow_user(current_user,user_to_follow):
        follow = Follows.objects.get_or_create(follower = current_user, following = user_to_follow)[0]
        follow.save()
    
    
    for user in user_data:
        add_user(user["user_name"],user["password"],user["location"],user["post_code"],user["phone"],user["reputation"])
    
    for book in book_data:
        user = User.objects.get(username=book["user_name"])
        user_profile = UserProfile.objects.get(user=user)
        add_book(user_profile,book["publisher"],book["author"],book["isbn"],book["title"],book["genre"])
    
    #link follers by username here
    follow_user(UserProfile.objects.get(user=User.objects.get(username="testuser1")),UserProfile.objects.get(user=User.objects.get(username="testuser2")))


if __name__=='__main__':
    print('Starting Book Share population script...') 
    populate()

 