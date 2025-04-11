

# Register your models here.
from django.contrib import admin
from .models import Book, Publication, Cart, CartItem

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'publication', 'stock')
    list_filter = ('publication',)
    search_fields = ('title', 'author')

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
    search_fields = ('name',)

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    inlines = [CartItemInline]

admin.site.register(Book, BookAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Cart, CartAdmin)