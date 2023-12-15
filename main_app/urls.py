from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('vinyls/', views.vinyls_index, name='index'),
  path('vinyls/<int:vinyl_id>/', views.vinyls_detail, name='detail'),
  path('vinyls/create/', views.VinylCreate.as_view(), name='vinyls_create'),
  path('vinyls/<int:pk>/update/', views.VinylUpdate.as_view(), name='vinyls_update'),
  path('vinyls/<int:pk>/delete/', views.VinylDelete.as_view(), name='vinyls_delete'),
  path('vinyls/<int:vinyl_id>/add_concert/', views.add_concert, name='add_concert'),
  path('vinyls/<int:vinyl_id>/add_genre/<int:genre_id>/', views.add_genre, name='add_genre'),
  path('vinyls/<int:vinyl_id>/remove_genre/<int:genre_id>/', views.remove_genre, name='remove_genre'),
  path('genres/', views.GenreList.as_view(), name='genres_index'),
  path('genres/<int:pk>/', views.GenreDetail.as_view(), name='genres_detail'),
  path('genres/create/', views.GenreCreate.as_view(), name='genres_create'),
  path('genres/<int:pk>/update/', views.GenreUpdate.as_view(), name='genres_update'),
  path('genres/<int:pk>/delete/', views.GenreDelete.as_view(), name='genres_delete'),
]