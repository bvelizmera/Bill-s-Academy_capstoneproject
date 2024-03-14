from django.shortcuts import render
from django.views import generic
from .models import Tournament

# Create your views here.
class TournamentList(generic.ListView):
    queryset = Tournament.objects.all()
    template_name = "tournament_list.html"