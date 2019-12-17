from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.users, name="users"),
    path('<int:pk>/', views.user_detail, name="user_detail"),
    path('<int:pk>/followers/', views.user_followers, name="user_followers"),
    path('<int:pk>/followings/', views.user_followings, name="user_followings"),
]
