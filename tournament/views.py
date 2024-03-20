from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Tournament, New
from .forms import ProfileForm
from .models import User, WebUser
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

def profile(request):
    profile = WebUser.objects.get_or_create(user=request.user)[0]
    return render(request, 'profile.html', {'profile':profile})

def edit_profile(request):
    profile = WebUser.objects.get_or_create(user=request.user)[0]
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

