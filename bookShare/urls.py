from django.urls import path 
from bookShare import views

app_name = 'bookShare'
urlpatterns = [
    path('', views.browse, name='browse'),
    path('browse/', views.browse, name='browse'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('<str:user_id>/profile/', views.profile, name='profile'),
    path('book/<str:book_id>/', views.book_info, name='book_info'),
    path('book/<str:book_id>/edit/', views.edit_book, name='edit_book'),
    path('book/<str:book_id>/add_interest/',views.add_interest, name="add_interest"),
    path('book/<str:book_id>/remove_interest/', views.remove_interest, name="remove_interest"),
    path('book/<str:book_id>/accept_interest/<str:reserved_user_id>/',views.accept_interest, name="accept_interest"),
    path('new_listing/', views.add_book, name='add_book'),
    path('search/', views.user_search, name = 'user_search'),
    path('<str:user_id>/profile/edit', views.edit_profile, name="edit_profile"),
    path('<str:user_id>/follow/', views.follow, name="follow"),
    path('<str:user_id>/unfollow/', views.unfollow, name="unfollow"),
    path('<str:user_id>/profile/followers', views.show_followers, name ="followers"),
    path('<str:user_id>/profile/following', views.show_following, name ="following"),
    path('webhook/',views.web_hook, name="webhook"),
]