from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Book, Publication, CartItem

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'price', 'publication', 'cover_image', 'stock']

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['name', 'address', 'website']

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']