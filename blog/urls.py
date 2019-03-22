from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.BlogHomeView.as_view(), name='blog-home'),
]
