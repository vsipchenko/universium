from django.urls import path

from movies.views import MoviesListView

urlpatterns = [
    path('', MoviesListView.as_view()),
]
