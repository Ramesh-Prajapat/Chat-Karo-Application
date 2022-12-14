from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('login/', views.login, name='login'),
    path('register_redirect/', views.register_redirect,name='register_redirect'),
    path('register/', views.register, name='register'),
    path('save/', views.save, name='save'),
    path('after_login/', views.after_login, name='after_login'),
    path('check_user/', views.check_user, name='check_user'),
    path('logout/', views.logout, name='logout'),
    path('navigation/', views.navigation, name='navigation'),
    path('chat/', views.chat, name='chat'),
    path('chat_sender/', views.chat_sender, name='chat_sender'),
    path('fetch/', views.fetch, name='fetch'),
    path('room/', views.room, name='room'),
    path('selectRoom/', views.selectRoom, name='selectRoom')
    ]
