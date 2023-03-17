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
    path('<str:book_id>/info/', views.book_info, name='book_info'),
    path('<str:genre>/<str:book_id>/edit/', views.edit_book, name='edit_book'),
    path('new_listing/', views.add_book, name='add_book'),
    path('search/', views.user_search, name = 'user_search'),
    path('<str:user_id>/profile/edit', views.edit_profile, name="edit_profile"),
    path('<str:user_id>/follow', views.follow, name="follow"),
    path('<str:user_id>/unfollow', views.unfollow, name="unfollow"),
    path('<str:user_id>/profile/followers', views.show_followers, name ="followers"),
    path('<str:user_id>/profile/following', views.show_following, name ="following"),
    path('<str:book_id>/add_intrest',views.add_intrest, name="add_intrest")
]