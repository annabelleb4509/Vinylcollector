from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Vinyl, Genre

from .forms import ConcertForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def vinyls_index(request):
  vinyls = Vinyl.objects.all()
  return render(request, 'vinyls/index.html', {
    'vinyls': vinyls
  })

def vinyls_detail(request, vinyl_id):
  vinyl = Vinyl.objects.get(id=vinyl_id)
  form = ConcertForm()
  genre_ids = vinyl.genres.all().values_list('id')
  available_genres = Genre.objects.exclude(id__in=genre_ids)
  return render(request, 'vinyls/detail.html', { 'vinyl': vinyl, 'form': form, 'available_genres': available_genres })

def add_concert(request, vinyl_id):
    form = ConcertForm(request.POST)
    if form.is_valid():
        new_concert = form.save(commit=False)
        new_concert.vinyl_id = vinyl_id
        new_concert.save()
    return redirect('detail', vinyl_id=vinyl_id)


def add_genre(request, vinyl_id, genre_id):
  vinyl = Vinyl.objects.get(id=vinyl_id).genres.add(genre_id)
  return redirect('detail', vinyl_id=vinyl_id)

def remove_genre(request, vinyl_id, genre_id):
  vinyl = Vinyl.objects.get(id=vinyl_id).genres.remove(genre_id)
  return redirect('detail', vinyl_id=vinyl_id)


class VinylCreate(CreateView):
  model = Vinyl
  fields = '__all__'

class VinylUpdate(UpdateView):
  model = Vinyl
  fields = ['artist', 'genre', 'released']

class VinylDelete(DeleteView):
  model = Vinyl
  success_url = '/vinyls'


class GenreList(ListView):
  model = Genre

class GenreDetail(DetailView):
  model = Genre

class GenreCreate(CreateView):
  model = Genre
  fields = ['name', 'description']

class GenreUpdate(UpdateView):
  model = Genre
  fields = ['name', 'description']

class GenreDelete(DeleteView):
  model = Genre
  success_url = '/genres'