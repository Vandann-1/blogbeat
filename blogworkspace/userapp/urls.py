from django.urls import path
from .views import *

urlpatterns = [
    
    path('',hh,name="hh"),
    path('register/',register,name="register"),
    path("home",home,name="home"),
    path("login/",loginview,name="login"),
    path("logout/",logoutview,name="logout"),


    path("helpspt",helSupport,name="helpspt"),
    path("settings",Settings,name="settings"),
]
