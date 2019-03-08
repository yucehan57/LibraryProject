from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('catalog/', views.BookListView.as_view(), name='book-list'),
]
