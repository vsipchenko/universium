import psycopg2.extras
from django.db import connection


def get_number_of_movies_by_genre(actor_id):
    query = '''
    select mg.genre   as genre,
           count(r.movie_id) as num_genres
      from roles as r
      join movies_genres as mg on r.movie_id = mg.movie_id
     where r.actor_id = %(actor_id)s
     group by r.actor_id, mg.genre
    '''
    with connection.cursor() as cursor:

        cursor.execute(query, {'actor_id': actor_id})
        return cursor.fetchall()
