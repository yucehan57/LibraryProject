from django.contrib import admin
from django.urls import path, include
from library_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library_app.urls')),
    path('contact/', views.ContactView.as_view(), name='contact-form'),
    path('success/', views.success_view, name='thanks'),
    path('accounts/', include('accounts.urls')),



]
