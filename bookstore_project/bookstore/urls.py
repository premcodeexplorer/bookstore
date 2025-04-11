from django.test import TestCase

# Create your tests here.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('cart/', views.cart, name='cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add-publication/', views.add_publication, name='add_publication'),
    path('add-book/', views.add_book, name='add_book'),
]