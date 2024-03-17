from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Tournament, New

# Create your views here.
class TournamentList(generic.ListView):
    queryset = Tournament.objects.all()
    template_name = "tournament_list.html"

class NewsList(generic.ListView):
    queryset = New.objects.filter(status=1)
    template_name = "new_list.html"

def tournament_detail(request, pk):
    """
    Shows tournament detials

    **Context**
    ``tournament`` instance of :model: `tournament.Tournament`

    **Template:**

    :template:`blog/tournament_detail.html`
    """

    queryset = Tournament.objects.all()
    tournament = get_object_or_404(queryset, pk=pk)

    return render(
        request,
        "tournament/tournament_detail.html",
        {"tournament": tournament},
    )

def new_detail(request, pk):
    """
    Shows tournament detials

    **Context**
    ``tournament`` instance of :model: `tournament.Tournament`

    **Template:**

    :template:`blog/tournament_detail.html`
    """

    queryset = New.objects.all()
    new = get_object_or_404(queryset, pk=pk)

    return render(
        request,
        "tournament/new_detail.html",
        {"new": new},
    )