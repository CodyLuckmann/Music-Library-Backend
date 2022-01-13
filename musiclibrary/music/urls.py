from django.urls import path
from . import views


urlpatterns = [
    path('127.0.0.1:8000/music/', views.SongList.as_view()),
    path('127.0.0.1:8000/music/<int:pk>/', views.SongDeatil.as_view()),
]