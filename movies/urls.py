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
        "lists/",
        views.my_lists,
        name="my_lists",
    ),

    path(
        "lists/create/",
        views.create_movie_list,
        name="create_movie_list",
    ),

    path(
        "lists/<int:list_id>/",
        views.movie_list_detail,
        name="movie_list_detail",
    ),

    path(
        "lists/<int:list_id>/add/<int:movie_id>/",
        views.add_movie_to_list,
        name="add_movie_to_list",
    ),

    path(
        "lists/<int:list_id>/remove/<int:movie_id>/",
        views.remove_movie_from_list,
        name="remove_movie_from_list",
    ),

    path(
        "lists/<int:list_id>/delete/",
        views.delete_movie_list,
        name="delete_movie_list",
    ),

    path(
        "about/",
        views.about,
        name="about",
    ),

    path(
    "join/",
    views.join,
    name="join",
),

]