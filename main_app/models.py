from django.db import models
from django.urls import reverse
from datetime import date

class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genres_detail', kwargs={'pk': self.id})


class Vinyl(models.Model):
    #properties/attributes/columns
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.TextField(max_length=100)
    released = models.IntegerField()

    genres = models.ManyToManyField(Genre)
    #methods (if needed)

    # __str__
    def __str__(self):
        return f'{self.title} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'vinyl_id': self.id})


class Concert(models.Model):
    date = models.DateField()
    city = models.CharField(
        max_length=100,
    )

    vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city} on {self.date}"

    class Meta:
        ordering = ['-date']

