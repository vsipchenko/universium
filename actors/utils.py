from actors.database import get_number_of_movies_by_genre


def get_actor_movies_statistics(actor_id):
    number_of_movies_by_genre = []
    top_genre = None
    movies_total = 0
    max_movies_by_genre = 0
    for genre, num_movies in get_number_of_movies_by_genre(actor_id):
        movies_total += num_movies
        if num_movies > max_movies_by_genre:
            top_genre = genre
            max_movies_by_genre = num_movies
        number_of_movies_by_genre.append({'num': num_movies, 'genre': genre})
    return {
        'number_of_movies': movies_total,
        'top_genre': top_genre,
        'number_of_movies_by_genre': number_of_movies_by_genre
    }
