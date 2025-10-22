from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Movie
from .forms import MovieForm

def index(request):
    return redirect('list_movies')

def list_movies(request):
    movies = Movie.objects.all()
    return render(request, 'list_movies.html', {'movies': movies})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie added successfully!')
            return redirect('list_movies')
    else:
        form = MovieForm()
        
    return render(request, 'add_movie.html', {'form': form})

def update_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, f'Movie "{movie.title}" updated successfully!')
            return redirect('list_movies')
    else:
        form = MovieForm(instance=movie)
        
    return render(request, 'update_movie.html', {'form': form, 'movie': movie})

def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    
    if request.method == 'POST':
        movie_title = movie.title
        movie.delete()
        messages.success(request, f'Movie "{movie_title}" deleted successfully!')
        return redirect('list_movies')
        
    return render(request, 'delete_movie.html', {'movie': movie})
