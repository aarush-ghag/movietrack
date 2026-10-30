from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import JoinForm, MovieListForm, WatchEntryForm
from .models import Movie, MovieList, WatchEntry


def home(request):
    return render(request, "movies/home.html")


def movie_list(request):
    query = request.GET.get("q", "").strip()

    movies = Movie.objects.all()

    if query:
        movies = movies.filter(title__icontains=query)

    movies = movies.order_by("title")

    return render(
        request,
        "movies/movie_list.html",
        {
            "movies": movies,
            "query": query,
        },
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


@login_required
def my_lists(request):
    movie_lists = MovieList.objects.filter(
        user=request.user
    ).order_by("name")

    return render(
        request,
        "movies/my_lists.html",
        {"movie_lists": movie_lists},
    )


@login_required
def create_movie_list(request):
    if request.method == "POST":
        form = MovieListForm(request.POST)

        if form.is_valid():
            movie_list = form.save(commit=False)
            movie_list.user = request.user
            movie_list.save()

            return redirect(
                "movie_list_detail",
                list_id=movie_list.id,
            )

    else:
        form = MovieListForm()

    return render(
        request,
        "movies/create_movie_list.html",
        {"form": form},
    )


@login_required
def movie_list_detail(request, list_id):
    movie_list = get_object_or_404(
        MovieList,
        id=list_id,
        user=request.user,
    )

    available_movies = Movie.objects.exclude(
        id__in=movie_list.movies.values_list(
            "id",
            flat=True,
        )
    ).order_by("title")

    return render(
        request,
        "movies/movie_list_detail.html",
        {
            "movie_list": movie_list,
            "available_movies": available_movies,
        },
    )


@login_required
def add_movie_to_list(request, list_id, movie_id):
    movie_list = get_object_or_404(
        MovieList,
        id=list_id,
        user=request.user,
    )

    movie = get_object_or_404(
        Movie,
        id=movie_id,
    )

    if request.method == "POST":
        movie_list.movies.add(movie)

    return redirect(
        "movie_list_detail",
        list_id=movie_list.id,
    )


@login_required
def remove_movie_from_list(request, list_id, movie_id):
    movie_list = get_object_or_404(
        MovieList,
        id=list_id,
        user=request.user,
    )

    movie = get_object_or_404(
        Movie,
        id=movie_id,
    )

    if request.method == "POST":
        movie_list.movies.remove(movie)

    return redirect(
        "movie_list_detail",
        list_id=movie_list.id,
    )


@login_required
def delete_movie_list(request, list_id):
    movie_list = get_object_or_404(
        MovieList,
        id=list_id,
        user=request.user,
    )

    if request.method == "POST":
        movie_list.delete()

    return redirect("my_lists")


def join(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = JoinForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("home")

    else:
        form = JoinForm()

    return render(
        request,
        "movies/join.html",
        {"form": form},
    )


def about(request):
    return render(request, "movies/about.html")