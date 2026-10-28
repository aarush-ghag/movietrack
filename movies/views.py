from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import WatchEntryForm
from .models import Movie, WatchEntry


def home(request):
    return render(request, "movies/home.html")


def movie_list(request):
    movies = Movie.objects.all().order_by("title")

    return render(
        request,
        "movies/movie_list.html",
        {"movies": movies},
    )


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    watch_entry = None

    if request.user.is_authenticated:
        watch_entry = WatchEntry.objects.filter(
            user=request.user,
            movie=movie,
        ).first()

    return render(
        request,
        "movies/movie_detail.html",
        {
            "movie": movie,
            "watch_entry": watch_entry,
        },
    )


@login_required
def add_to_watchlist(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    WatchEntry.objects.get_or_create(
        user=request.user,
        movie=movie,
        defaults={"status": "want_to_watch"},
    )

    return redirect("movie_detail", movie_id=movie.id)


@login_required
def watchlist(request):
    want_to_watch = WatchEntry.objects.filter(
        user=request.user,
        status="want_to_watch",
    ).select_related("movie").order_by("movie__title")

    watched = WatchEntry.objects.filter(
        user=request.user,
        status="watched",
    ).select_related("movie").order_by("movie__title")

    return render(
        request,
        "movies/watchlist.html",
        {
            "want_to_watch": want_to_watch,
            "watched": watched,
        },
    )


@login_required
def edit_watch_entry(request, entry_id):
    entry = get_object_or_404(
        WatchEntry,
        id=entry_id,
        user=request.user,
    )

    if request.method == "POST":
        form = WatchEntryForm(
            request.POST,
            instance=entry,
        )

        if form.is_valid():
            form.save()
            return redirect("watchlist")

    else:
        form = WatchEntryForm(instance=entry)

    return render(
        request,
        "movies/edit_watch_entry.html",
        {
            "form": form,
            "entry": entry,
        },
    )


@login_required
def remove_from_watchlist(request, entry_id):
    entry = get_object_or_404(
        WatchEntry,
        id=entry_id,
        user=request.user,
    )

    if request.method == "POST":
        entry.delete()

    return redirect("watchlist")


def about(request):
    return render(request, "movies/about.html")