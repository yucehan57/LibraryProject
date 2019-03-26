from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.PostHomeView.as_view(), name='blog-home'),
    path('<int:pk>', views.PostDetailView.as_view(), name='blog-detail'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='blog-update'),
]
