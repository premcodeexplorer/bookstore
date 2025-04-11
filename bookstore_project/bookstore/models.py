

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Publication(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    website = models.URLField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart #{self.id} - {self.user.username}"

    def total_price(self):
        return sum(item.total_price() for item in self.cartitem_set.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.quantity} x {self.book.title}"

    def total_price(self):
        return self.quantity * self.book.price