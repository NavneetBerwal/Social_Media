from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.feed, name='home'),
    path('post/', views.post),
    path('registration/', views.registration, name='registration'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('feed/', views.feed, name='feed')


]
