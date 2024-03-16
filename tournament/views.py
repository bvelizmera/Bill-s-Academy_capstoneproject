from django.shortcuts import render
from django.views import generic
from .models import Tournament, New

# Create your views here.
class TournamentList(generic.ListView):
    queryset = Tournament.objects.all()
    template_name = "tournament_list.html"
    paginated_by = 2

class NewsList(generic.ListView):
    queryset = New.objects.all()
    template_name = "new_list.html"