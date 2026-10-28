from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path(
        "movies/",
        views.movie_list,
        name="movie_list",
    ),

    path(
        "movies/<int:movie_id>/",
        views.movie_detail,
        name="movie_detail",
    ),

    path(
        "movies/<int:movie_id>/add/",
        views.add_to_watchlist,
        name="add_to_watchlist",
    ),

    path(
        "watchlist/",
        views.watchlist,
        name="watchlist",
    ),

    path(
        "watchlist/<int:entry_id>/edit/",
        views.edit_watch_entry,
        name="edit_watch_entry",
    ),

    path(
        "watchlist/<int:entry_id>/remove/",
        views.remove_from_watchlist,
        name="remove_from_watchlist",
    ),

    path(
        "about/",
        views.about,
        name="about",
    ),
]