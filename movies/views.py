from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from movies.models import Movie, MovieDirector, MovieGenre
from movies.serializers import MovieSerializer


class MoviesListView(APIView):
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination

    def get(self, request):
        movies = Movie.objects.all()
        director_id = request.GET.get('director')
        if director_id:
            director_movies = MovieDirector.objects.filter(director_id=director_id).values_list('movie_id')
            movies = movies.filter(id__in=director_movies)
        genre = request.GET.get('genre')
        if genre:
            movies_genres = MovieGenre.objects.filter(genre=genre).values_list('movie_id')
            movies = movies.filter(id__in=movies_genres)

        serializer = self.serializer_class(movies, many=True)
        return Response(serializer.data)
