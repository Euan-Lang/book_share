from django.contrib.auth.models import User
from bookShare.models import UserProfile
from django import forms


class UserForm(forms.ModelForm):
    username = forms.CharField(label="username",
                               widget=forms.TextInput(attrs={"placeholder": "your username"}))
    email = forms.EmailField(label="email",
                             widget=forms.EmailInput(attrs={"placeholder": "yourname@example.com"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "********"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    location = forms.CharField(label="location",
                               widget=forms.TextInput(attrs={"placeholder": "Exampleville"}))
    post_code = forms.CharField(label="post_code",
                                widget=forms.TextInput(attrs={"placeholder": "XXXXXX"}))
    phone_number = forms.CharField(label="phone_number",
                                   widget=forms.TextInput(attrs={"placeholder": "01234567901"}))

    class Meta:
        model = UserProfile
        fields = ('location', 'post_code', 'phone_number', 'user_image')
