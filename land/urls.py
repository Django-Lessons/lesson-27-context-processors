from django.urls import path

from land import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.user_profile, name='user_profile'),
    path('login', views.login, name='login'),
    path('privacy', views.privacy_policy, name='privacy'),
]
