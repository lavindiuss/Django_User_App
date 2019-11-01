from django.urls import path
from django.conf.urls import include
from . import views
from rest_framework.response import Response






urlpatterns = [
    path('UserView/', views.UserViews.as_view(), name='user-view'),
    path('UserLogIn/', views.LogInView.as_view(), name='user-login'),

]
