from django.contrib import admin
from .models import Genre, Book, Author, BookInstance
# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(BookInstance)


# register Author model
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

# Register the admin class with the associated model
# admin.site.register(Author, AuthorAdmin)
# @admin.register(modelName) has the same functionality as the one above.

# class BookInstanceInline(admin.TabularInline):
#     model = BookInstance


# register Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('author', 'genre')
    # inlines = [BookInstanceInline]

# register BookInstance model
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'imprint', 'id')
    list_filter = ('status', 'due_back', 'imprint')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

#register Genre model
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
