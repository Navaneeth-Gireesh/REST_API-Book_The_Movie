from django.shortcuts import render
from .serializers import MovieSerializer
from rest_framework import viewsets
from . models import MoviesData
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.all()
    serializer_class = MovieSerializer

class ActionMovieViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(genere='Action')
    serializer_class = MovieSerializer

class SciFiMovieViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(genere = 'Sci-Fi')
    serializer_class = MovieSerializer

class ComedyMovieViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(genere = 'Comedy')
    serializer_class = MovieSerializer

class PsychologicalDramaMovieViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(genere = 'Psychological Drama')
    serializer_class = MovieSerializer