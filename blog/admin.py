from django.contrib import admin
from .models import Author, Post

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    search_fields = ['title', 'author__name']
    list_filter = ['author', 'created_at']
    readonly_fields = ['viewers']
