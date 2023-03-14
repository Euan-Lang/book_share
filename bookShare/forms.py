from django.contrib.auth.models import User
from bookShare.models import UserProfile, Book
from django import forms


class UserForm(forms.ModelForm):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(attrs={"placeholder": "your username"}))
    email = forms.EmailField(label="Email",
                             widget=forms.EmailInput(attrs={"placeholder": "yourname@example.com"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "********"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    location = forms.CharField(label="Location",
                               widget=forms.TextInput(attrs={"placeholder": "Exampleville"}))
    post_code = forms.CharField(label="Post Code",
                                widget=forms.TextInput(attrs={"placeholder": "XXXXXX"}))
    phone_number = forms.CharField(label="Phone No.",
                                   widget=forms.TextInput(attrs={"placeholder": "01234567901"}))
    
    user_image = forms.ImageField(label="Profile Picture")

    class Meta:
        model = UserProfile
        fields = ('location', 'post_code', 'phone_number', 'user_image')

class BookForm(forms.ModelForm):
    title = forms.CharField(label="Title",widget=forms.TextInput(attrs={"placeholder": "Harry Potter"}))
    publisher = forms.CharField(label="Publisher",widget=forms.TextInput(attrs={"placeholder": "Bloomsbury"}))
    author = forms.CharField(label="Author",widget=forms.TextInput(attrs={"placeholder": "JK Rowling"}))
    isbn = forms.CharField(label="ISBN",widget=forms.TextInput(attrs={"placeholder": "9780747532743"}))
    cover_image = forms.ImageField(label="Cover Image",required=False)
    genre = forms.CharField(label="Genre",widget=forms.TextInput(attrs={"placeholder": "Fantasy"}))

    class Meta:
        model = Book
        fields = ('title','publisher','author','isbn','cover_image','genre')