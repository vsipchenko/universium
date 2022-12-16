from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=256)
    year = models.IntegerField()
    rank = models.FloatField()

    class Meta:
        db_table = 'movies'


class MovieGenre(models.Model):
    movie_id = models.ForeignKey('Movie', on_delete=models.DO_NOTHING)
    genre = models.CharField(max_length=256)

    class Meta:
        db_table = 'movies_genres'


class MovieDirector(models.Model):
    director_id = models.ForeignKey('actors.Director', on_delete=models.DO_NOTHING)
    movie_id = models.ForeignKey('Movie', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'movies_directors'
