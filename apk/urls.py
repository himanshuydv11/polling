from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('location/', views.location, name='location'),
    path('signup', views.usersignup, name='signup'),
    path('login', views.loginhere, name='login'),
    path('logout', views.logouthere, name='logout'),
    path('profile', views.profile, name='profile'),
    path('profile/create', views.create_poll, name='create'),
]
