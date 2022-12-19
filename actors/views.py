from rest_framework.response import Response
from rest_framework.views import APIView

from actors.models import Actor


class ActorsStatsView(APIView):
    def get(self, request, pk):
        actors = Actor.objects.all()
        return Response('ok')
