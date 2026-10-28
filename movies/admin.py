from django.contrib import admin

from .models import Movie, WatchEntry, MovieList


admin.site.register(Movie)
admin.site.register(WatchEntry)
admin.site.register(MovieList)