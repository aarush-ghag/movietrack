from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class WatchEntry(models.Model):
    STATUS_CHOICES = [
        ("want_to_watch", "Want to Watch"),
        ("watched", "Watched"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="want_to_watch"
    )
    rating = models.IntegerField(null=True, blank=True)
    review = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"


class MovieList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, blank=True)

    def __str__(self):
        return self.name