from django.urls import path 
from bookShare import views
app_name = 'bookShare'
urlpatterns = [
    path('', views.index, name='index'),
]