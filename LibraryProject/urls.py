from django.contrib import admin
from django.urls import path, include
from library_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library_app.urls')),
    path('email', views.email_view, name='email'),
    path('success', views.success_view, name='success'),
]
