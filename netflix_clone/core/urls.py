from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('profiles', views.profiles, name="profiles"),
    path('movie/<str:pk>/', views.movie, name="movie"),
    path('search', views.search, name="search"),
    path('my-list', views.my_list, name="my-list"),
    path('add-to-list', views.add_to_list, name="add-to-list"),
    path('genre/<str:pk>/', views.genre, name="genre"),
    path('logout', views.logout, name="logout"),
]