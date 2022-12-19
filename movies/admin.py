from django.contrib import admin

from movies.models import Movie, MovieGenre

admin.site.register(Movie)
admin.site.register(MovieGenre)