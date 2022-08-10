from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.userlogin, name='home'),
    path('post/', views.post, name ='post'),
    path('registration/', views.registration, name='registration'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('feed/', views.feed, name='feed'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('profile/', views.profile, name='profile'),
    path('like/<str:pk>', views.like, name='like'),
    path('unlike/<str:pk>', views.unlike, name='unlike'),
    path('profile/', views.profile, name='profile'),
    path('feed/comments/<int:id>', views.comments, name='comments'),
]
