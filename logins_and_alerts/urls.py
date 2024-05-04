from django.urls import path

from . import views

app_name = 'loginsapp' 
urlpatterns = [
    path("signin/", views.loginuser, name="loginuser"),
    path("signout/", views.logoutuser, name="logoutuser"),
]