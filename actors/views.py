from rest_framework.response import Response
from rest_framework.views import APIView


class ActorsStatsView(APIView):
    def get(self, request, pk):
        return Response('ok')
