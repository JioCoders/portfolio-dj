from django.urls import path
from . import views

# Define URL patterns for the tweet app

urlpatterns = [
    # path('', views.index, name='index'),  # Default route to index view
    path('', views.tweet_list, name='tweet_list'),  # Default route to index view
    path('create/', views.tweet_create, name='tweet_create'), # Route to create a new tweet
    path('<int:pk>/', views.tweet_detail, name='tweet_detail'),
    path('<int:pk>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:pk>/delete/', views.tweet_delete, name='tweet_delete'),

    path('register/', views.register, name='register'),  # Route for user registration
    # path('login/', views.user_login, name='login'),  # Route for user login
    # path('logout/', views.user_logout, name='logout'),  # Route for user logout
    # path('profile/<str:username>/', views.profile, name='profile'),  # Route for user profiles
    # Add more paths as needed
]