from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("test/", test, name="test"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("registration/", registration, name="registration"),
    path("profile/<int:pk>/", profile, name="profile"),
    path("retailers/", retailers, name="retailers"),
    path("password_change/", password_change, name="password_change"),
    
      
]

