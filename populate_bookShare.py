import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','book_share.settings')
import django
from django.core.files.images import ImageFile
django.setup() 
from bookShare.models import UserProfile,User,Follows,Book
from django.contrib.auth.hashers import make_password

def populate():
    #add user data here
    user_data=[
            {"user_name":"testuser1",
            "password":make_password("Hello123"),
            "email":"testuser1@gmail.com",
            "location":"Hamilton",
            "post_code":"ML38LT",
            "phone":"07986851525",
            "reputation":0,
            "img_name":"",
            },
            {
            "user_name":"testuser2",
            "password":make_password("hello123456789"),
            "email":"testuser2@gmail.com",
            "location":"Hamilton",
            "post_code":"ML36PZ",
            "phone":"01698365241",
            "reputation":43,
            "img_name":"",
            },
            {
            "user_name":"Jim",
            "password":make_password("hello123456789"),
            "email":"Jim@gmail.com",
            "location":"Hillhead",
            "post_code":"G128SP",
            "phone":"07986851527",
            "reputation":74,
            "img_name":"jim.jpg",
            },
            {
            "user_name":"Lindsey",
            "password":make_password("hello123456789"),
            "email":"Lindsey@gmail.com",
            "location":"Glasgow",
            "post_code":"G13SL",
            "phone":"07986851528",
            "reputation":32,
            "img_name":"lindsey.jpg",
            },
            {
            "user_name":"Andrew",
            "password":make_password("hello123456789"),
            "email":"Andrew@gmail.com",
            "location":"Partick",
            "post_code":"G116TG",
            "phone":"07986851529",
            "reputation":50,
            "img_name":"andrew.jpg",
            },

        ]
    #add book data here
    book_data=[
        {"user_name":"testuser1",
         "publisher":"MnM Publishing",
         "author":"john williamson",
         "isbn":"2463472534658",
         "title":"CS1P - Introduction",
         "genre":"computing science",
         "img_name":""
        },
        {"user_name":"testuser2",
         "publisher":"HarperCollins",
         "author":"J.R.R. Tolkien",
         "isbn":"9780007458424",
         "title":"The Hobbit",
         "genre":"fantasy",
         "img_name":"IMG_20230316_210130.jpg"
        },
        {"user_name":"Jim",
         "publisher":"Award Publications",
         "author":"Jules Verne",
         "isbn":"9781782700432",
         "title":"A Journey to the Centre of the Earth",
         "genre":"fantasy",
         "img_name":"IMG_20230316_210144.jpg"
        },
        {"user_name":"Lindsey",
         "publisher":"Puffin Books",
         "author":"Maurice Gee",
         "isbn":"9780143305019",
         "title":"Under the Mountain",
         "genre":"fantasy",
         "img_name":"IMG_20230316_210159.jpg"
        },
        {"user_name":"Andrew",
         "publisher":"Floris Books",
         "author":"Kathleen Fidler",
         "isbn":"9780863158827",
         "title":"The Boy with the Bronze Axe",
         "genre":"historical fiction",
         "img_name":"IMG_20230316_210213.jpg"
        },
        {"user_name":"testuser1",
         "publisher":"John Murray (Publishers)",
         "author":"Randall Munroe",
         "isbn":"9781848549562",
         "title":"What If?",
         "genre":"comedy",
         "img_name":"IMG_20230316_210302.jpg"
        },
        {"user_name":"testuser2",
         "publisher":"John Murray (Publishers)",
         "author":"Randall Munroe",
         "isbn":"9781473680340",
         "title":"How To",
         "genre":"comedy",
         "img_name":"IMG_20230323_100641.jpg"
        },
        {"user_name":"testuser2",
         "publisher":"Quirk Books",
         "author":"Ian Doescher",
         "isbn":"9781594747151",
         "title":"William Shakespeare's The Empire Striketh Back",
         "genre":"science fiction",
         "img_name":"IMG_20230316_210344.jpg"
        },
        {"user_name":"Jim",
         "publisher":"Pan Macmillan",
         "author":"George Orwell",
         "isbn":"9781529032666",
         "title":"Nineteen Eighty-Four",
         "genre":"dystopian",
         "img_name":"IMG_20230316_210359.jpg"
        },
        {"user_name":"Lindsey",
         "publisher":"Quercus Editions",
         "author":"Paul Glendinning",
         "isbn":"9781780873695",
         "title":"Maths in Minutes",
         "genre":"mathematics",
         "img_name":"IMG_20230316_210422.jpg"
        },
        {"user_name":"Andrew",
         "publisher":"Bloomsbury Publishing",
         "author":"Peter Holden and Tim Cleeves",
         "isbn":"9781472906472",
         "title":"RSPB Handbook of British Birds",
         "genre":"wildlife",
         "img_name":"IMG_20230316_210443.jpg"
        },
        {"user_name":"testuser1",
         "publisher":"Swan Hill Press",
         "author":"Peter Toghill",
         "isbn":"9781840374049",
         "title":"The Geology of Britain: An Introduction",
         "genre":"geography",
         "img_name":"IMG_20230316_210507.jpg"
        },
        {"user_name":"testuser2",
         "publisher":"British Geological Survey",
         "author":"British Geological Survey",
         "isbn":"9780751835021",
         "title":"Bedrock Geology: UK North",
         "genre":"geography",
         "img_name":"IMG_20230316_220915.jpg"
        },
        {"user_name":"Jim",
         "publisher":"Whitcombe and Tombs Limited",
         "author":"C.A. Cotton",
         "isbn":"",
         "title":"Geomorphology: An Introduction to the Study of Landforms",
         "genre":"geography",
         "img_name":"IMG_20230316_220947.jpg"
        },
        {"user_name":"Jim",
         "publisher":"HarperCollins",
         "author":"J.R.R. Tolkien",
         "isbn":"9780261102354",
         "title":"The Lord of the Rings - The Fellowship of the Ring",
         "genre":"fantasy",
         "img_name":"IMG_20230323_100657.jpg"
        },
        {"user_name":"Andrew",
         "publisher":"HarperCollins",
         "author":"J.R.R. Tolkien",
         "isbn":"9780261102361",
         "title":"The Lord of the Rings - The Two Towers",
         "genre":"fantasy",
         "img_name":"IMG_20230323_100707.jpg"
        },
        {"user_name":"Lindsey",
         "publisher":"HarperCollins",
         "author":"J.R.R. Tolkien",
         "isbn":"9780261102378",
         "title":"The Lord of the Rings - The Return of the King",
         "genre":"fantasy",
         "img_name":"IMG_20230323_100805.jpg"
        },
        {"user_name":"Jim",
         "publisher":"Geoffrey Bles",
         "author":"C.S. Lewis",
         "isbn":"",
         "title":"The Screwtape Letters",
         "genre":"theology",
         "img_name":"IMG_20230323_102333.jpg"
        },
    ]


    def add_user(user_name,password,email,location,post_code,phone,reputation,img_name):
        user = User.objects.get_or_create(username=user_name, password=password,email=email)[0]
        userProfile = UserProfile.objects.get_or_create(user=user,location=location,post_code=post_code,reputation=reputation,phone_number=phone)[0]
        if img_name and not userProfile.user_image:
            userProfile.user_image = ImageFile(open(os.path.join("populate_media",img_name), "rb"))
        userProfile.save()

    def add_book(user,publisher,author,isbn,title,genre,img_name):
        book = Book.objects.get_or_create(user_profile = user,publisher=publisher,author=author,title=title,genre=genre)[0]
        if img_name and not book.cover_image:
            book.cover_image = ImageFile(open(os.path.join("populate_media",img_name), "rb"))
        if isbn:
            book.isbn = isbn
        else:
            book.isbn = None
        book.save()
        
    def follow_user(current_user,user_to_follow):
        follow = Follows.objects.get_or_create(follower = current_user, following = user_to_follow)[0]
        follow.save()
    
    print("Populating users...")
    for user in user_data:
        add_user(user["user_name"],user["password"],user["email"],user["location"],user["post_code"],user["phone"],user["reputation"],user["img_name"])
    
    print("Populating books...")
    for book in book_data:
        user = User.objects.get(username=book["user_name"])
        user_profile = UserProfile.objects.get(user=user)
        add_book(user_profile,book["publisher"],book["author"],book["isbn"],book["title"],book["genre"],book["img_name"])
    
    #link follers by username here
    follow_user(UserProfile.objects.get(user=User.objects.get(username="testuser1")),UserProfile.objects.get(user=User.objects.get(username="testuser2")))


if __name__=='__main__':
    print('Starting Book Share population script...') 
    populate()
