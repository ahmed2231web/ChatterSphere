from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_home, name='chat_home'),
    path('<str:room_name>/', views.chat_room, name='chat_room'),
]