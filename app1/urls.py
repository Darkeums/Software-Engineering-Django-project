from django.urls import path
from . import views

# Defines the application namespace (optional but good practice)
# app_name = 'app1' 

urlpatterns = [
    # C - Create
    path('movies/add/', views.add_movie, name='add_movie'),
    
    # R - Read 
    path('', views.index, name='index'), # Root path, redirects to list_movies
    path('movies/', views.list_movies, name='list_movies'),
    
    # U - Update
    path('movies/<int:pk>/update/', views.update_movie, name='update_movie'),
    
    # D - Delete
    path('movies/<int:pk>/delete/', views.delete_movie, name='delete_movie'),
]
