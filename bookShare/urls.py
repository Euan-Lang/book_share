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
    path('<str:genre>/<str:book_id>/', views.book_info, name='book_info'),
    path('<str:genre>/<str:book_id>/edit/', views.edit_book, name='edit_book'),
    path('new_listing/', views.add_book, name='add_book'),
]