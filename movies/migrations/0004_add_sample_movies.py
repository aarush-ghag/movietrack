from django.db import migrations


MOVIES = [
    ("The Godfather", 1972, "Crime / Drama"),
    ("The Godfather Part II", 1974, "Crime / Drama"),
    ("Taxi Driver", 1976, "Drama / Crime"),
    ("Jaws", 1975, "Thriller / Adventure"),
    ("Rocky", 1976, "Drama / Sports"),
    ("Star Wars", 1977, "Science Fiction / Adventure"),
    ("Alien", 1979, "Science Fiction / Horror"),
    ("Apocalypse Now", 1979, "War / Drama"),
    ("The Shining", 1980, "Horror"),
    ("Raiders of the Lost Ark", 1981, "Adventure / Action"),
    ("The Thing", 1982, "Science Fiction / Horror"),
    ("Blade Runner", 1982, "Science Fiction / Thriller"),
    ("Scarface", 1983, "Crime / Drama"),
    ("Back to the Future", 1985, "Science Fiction / Comedy"),
    ("Aliens", 1986, "Science Fiction / Action"),
    ("Platoon", 1986, "War / Drama"),
    ("Full Metal Jacket", 1987, "War / Drama"),
    ("Die Hard", 1988, "Action / Thriller"),
    ("Goodfellas", 1990, "Crime / Drama"),
    ("The Silence of the Lambs", 1991, "Thriller / Crime"),
    ("Terminator 2: Judgment Day", 1991, "Science Fiction / Action"),
    ("Reservoir Dogs", 1992, "Crime / Thriller"),
    ("Jurassic Park", 1993, "Science Fiction / Adventure"),
    ("Schindler's List", 1993, "Historical Drama"),
    ("The Shawshank Redemption", 1994, "Drama"),
    ("Pulp Fiction", 1994, "Crime / Drama"),
    ("Forrest Gump", 1994, "Drama / Comedy"),
    ("Se7en", 1995, "Crime / Thriller"),
    ("Heat", 1995, "Crime / Thriller"),
    ("Toy Story", 1995, "Animation / Adventure"),
    ("Fargo", 1996, "Crime / Drama"),
    ("Titanic", 1997, "Romance / Drama"),
    ("Good Will Hunting", 1997, "Drama"),
    ("Saving Private Ryan", 1998, "War / Drama"),
    ("The Truman Show", 1998, "Drama / Comedy"),
    ("The Big Lebowski", 1998, "Comedy / Crime"),
    ("The Matrix", 1999, "Science Fiction / Action"),
    ("Fight Club", 1999, "Drama"),
    ("The Green Mile", 1999, "Drama / Fantasy"),
    ("American Beauty", 1999, "Drama"),
    ("Gladiator", 2000, "Action / Drama"),
    ("Memento", 2000, "Mystery / Thriller"),
    ("Cast Away", 2000, "Drama / Adventure"),
    ("The Lord of the Rings: The Fellowship of the Ring", 2001, "Fantasy / Adventure"),
    ("A Beautiful Mind", 2001, "Drama / Biography"),
    ("Spirited Away", 2001, "Animation / Fantasy"),
    ("The Lord of the Rings: The Two Towers", 2002, "Fantasy / Adventure"),
    ("Catch Me If You Can", 2002, "Crime / Drama"),
    ("City of God", 2002, "Crime / Drama"),
    ("The Lord of the Rings: The Return of the King", 2003, "Fantasy / Adventure"),
    ("Finding Nemo", 2003, "Animation / Adventure"),
    ("Kill Bill: Vol. 1", 2003, "Action / Crime"),
    ("Eternal Sunshine of the Spotless Mind", 2004, "Romance / Science Fiction"),
    ("The Incredibles", 2004, "Animation / Action"),
    ("Batman Begins", 2005, "Action / Crime"),
    ("V for Vendetta", 2005, "Action / Drama"),
    ("The Departed", 2006, "Crime / Thriller"),
    ("The Prestige", 2006, "Drama / Mystery"),
    ("No Country for Old Men", 2007, "Crime / Thriller"),
    ("There Will Be Blood", 2007, "Drama"),
    ("Ratatouille", 2007, "Animation / Comedy"),
    ("The Dark Knight", 2008, "Action / Crime"),
    ("WALL-E", 2008, "Animation / Science Fiction"),
    ("Inglourious Basterds", 2009, "War / Drama"),
    ("Up", 2009, "Animation / Adventure"),
    ("Avatar", 2009, "Science Fiction / Adventure"),
    ("Inception", 2010, "Science Fiction / Thriller"),
    ("Shutter Island", 2010, "Mystery / Thriller"),
    ("Toy Story 3", 2010, "Animation / Adventure"),
    ("Drive", 2011, "Crime / Drama"),
    ("The Intouchables", 2011, "Drama / Comedy"),
    ("Django Unchained", 2012, "Western / Drama"),
    ("The Avengers", 2012, "Action / Science Fiction"),
    ("The Wolf of Wall Street", 2013, "Biography / Comedy"),
    ("Her", 2013, "Romance / Science Fiction"),
    ("Prisoners", 2013, "Crime / Thriller"),
    ("Interstellar", 2014, "Science Fiction / Drama"),
    ("Whiplash", 2014, "Drama / Music"),
    ("Gone Girl", 2014, "Mystery / Thriller"),
    ("Mad Max: Fury Road", 2015, "Action / Science Fiction"),
    ("The Revenant", 2015, "Adventure / Drama"),
    ("The Hateful Eight", 2015, "Western / Drama"),
    ("Deadpool", 2016, "Action / Comedy"),
    ("La La Land", 2016, "Musical / Romance"),
    ("Arrival", 2016, "Science Fiction / Drama"),
    ("Get Out", 2017, "Horror / Thriller"),
    ("Blade Runner 2049", 2017, "Science Fiction / Drama"),
    ("Dunkirk", 2017, "War / Drama"),
    ("Avengers: Infinity War", 2018, "Action / Science Fiction"),
    ("Spider-Man: Into the Spider-Verse", 2018, "Animation / Action"),
    ("Parasite", 2019, "Thriller / Drama"),
    ("Joker", 2019, "Crime / Drama"),
    ("Avengers: Endgame", 2019, "Action / Science Fiction"),
    ("1917", 2019, "War / Drama"),
    ("Dune", 2021, "Science Fiction / Adventure"),
    ("The Batman", 2022, "Crime / Action"),
    ("Top Gun: Maverick", 2022, "Action / Drama"),
    ("Everything Everywhere All at Once", 2022, "Science Fiction / Comedy"),
    ("Oppenheimer", 2023, "Biography / Drama"),
    ("Dune: Part Two", 2024, "Science Fiction / Adventure"),
]


def add_sample_movies(apps, schema_editor):
    Movie = apps.get_model("movies", "Movie")

    for title, release_year, genre in MOVIES:
        Movie.objects.update_or_create(
            title=title,
            defaults={
                "release_year": release_year,
                "genre": genre,
                "description": (
                    f"{title} is a {genre.lower()} film released in "
                    f"{release_year}. Add it to your watchlist, mark it "
                    "as watched, rate it, review it, or organize it "
                    "into one of your custom MovieTrack lists."
                ),
            },
        )


def remove_sample_movies(apps, schema_editor):
    Movie = apps.get_model("movies", "Movie")

    Movie.objects.filter(
        title__in=[movie[0] for movie in MOVIES]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_movielist"),
    ]

    operations = [
        migrations.RunPython(
            add_sample_movies,
            remove_sample_movies,
        ),
    ]