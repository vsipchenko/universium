from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from actors.models import Actor
from utils import get_actor_movies_statistics


class ActorsStatsView(APIView):
    def get(self, request, pk):
        actor_data = Actor.objects.filter(id=pk).values('id', 'first_name', 'last_name').first()
        if not actor_data:
            return Response(f'User with id {pk} does not exist', status=status.HTTP_404_NOT_FOUND)

        actor_statistics = get_actor_movies_statistics(pk)
        # TODO most_frequent_partner implementation
        return Response({**actor_data, **actor_statistics})
