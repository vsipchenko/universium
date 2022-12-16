from django.urls import path

from actors.views import ActorsStatsView

urlpatterns = [
    path('<int:pk>/stats/', ActorsStatsView.as_view()),
]
