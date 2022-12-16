from django.db import models


class Actor(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    gender = models.CharField(max_length=256, choices=GENDER_CHOICES)

    class Meta:
        db_table = 'actors'


class Role(models.Model):
    actor_id = models.ForeignKey('Actor', on_delete=models.DO_NOTHING)
    movie_id = models.ForeignKey('movies.Movie', on_delete=models.DO_NOTHING)
    role = models.CharField(max_length=256)

    class Meta:
        db_table = 'roles'


class Director(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    class Meta:
        db_table = 'directors'


class DirectorGenre(models.Model):
    director_id = models.ForeignKey('Director', on_delete=models.DO_NOTHING)
    genre = models.CharField(max_length=256)
    prob = models.FloatField()

    class Meta:
        db_table = 'directors_genres'
