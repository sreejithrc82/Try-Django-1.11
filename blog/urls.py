from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name = 'blog-home'),
    path('about/', views.about, name='blog-about'),
    path('login/', views.login, name='blog-login'),
]
