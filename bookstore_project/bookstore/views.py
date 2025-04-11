

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book, Publication, Cart, CartItem
from .forms import UserRegisterForm, UserLoginForm, BookForm, PublicationForm, CartItemForm

def home(request):
    books = Book.objects.all()
    return render(request, 'bookstore/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            if request.user.is_authenticated:
                cart, created = Cart.objects.get_or_create(user=request.user)
                cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
                if not created:
                    cart_item.quantity += quantity
                else:
                    cart_item.quantity = quantity
                cart_item.save()
                messages.success(request, f"{book.title} added to your cart!")
                return redirect('cart')
            else:
                messages.warning(request, "Please login to add items to cart")
                return redirect('login')
    else:
        form = CartItemForm()
    return render(request, 'bookstore/book_detail.html', {'book': book, 'form': form})

@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    total = cart.total_price()
    return render(request, 'bookstore/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, "Item removed from cart")
    return redirect('cart')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'bookstore/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'bookstore/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

@login_required
def add_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Publication added successfully!")
            return redirect('home')
    else:
        form = PublicationForm()
    return render(request, 'bookstore/add_publication.html', {'form': form})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'bookstore/add_book.html', {'form': form})