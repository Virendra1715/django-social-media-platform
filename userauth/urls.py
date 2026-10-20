from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("signup/", views.signup, name="signup"),
    path("loginn/", views.loginn, name="loginn"),
    path("logout/", views.logoutt, name="logout"),

    path("search/", views.search_results, name="search_results"),

    path("upload/", views.upload, name="upload"),

    path("like-post/<str:id>/", views.likes, name="like_post"),

    path("explore/", views.explore, name="explore"),

    path(
        "profile/<str:id_user>/",
        views.profile,
        name="profile"
    ),
    path('follow',views.follow,name='follow'),
]