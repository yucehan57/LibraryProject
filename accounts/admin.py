from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """added for test reasons. Will be erased"""
    list_display = ('username', 'first_name', 'last_name')
    list_filter = ('username', 'first_name', 'last_name')
