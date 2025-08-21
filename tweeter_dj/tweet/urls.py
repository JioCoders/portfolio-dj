from django.urls import path
from . import views

# Define URL patterns for the tweet app

urlpatterns = [
    path('', views.index, name='index'),  # Default route to index view
    # path('', views.tweet_list, name='tweet_list'),  # Default route to index view
    # path('create/', views.tweet_create, name='tweet_create'), # Route to create a new tweet
    # path('<int:pk>/', views.tweet_detail, name='tweet_detail'),
    # path('<int:pk>/edit/', views.tweet_edit, name='tweet_edit'),
    # path('<int:pk>/delete/', views.tweet_delete, name='tweet_delete'),
    # Add more paths as needed
]