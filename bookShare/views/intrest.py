from bookShare.models import Intrest, UserProfile, Book
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required