from django.urls import path
from.views import register,home,user_login
urlpatterns = [
    path("",register),
    path("login",user_login,name="user_login"),
    path("home",home,name="home1")
]
