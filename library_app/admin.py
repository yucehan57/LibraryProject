from django.contrib import admin
from .models import Genre, Book, Author
# Register your models here.
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
