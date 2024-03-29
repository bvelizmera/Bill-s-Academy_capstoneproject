from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from .models import Tournament, New
from .forms import ProfileForm, TournamentForm, NewForm
from .models import User, WebUser, Tournament
from django.urls import reverse
import cloudinary.uploader
from django.contrib import messages
# Create your views here.






def homepage(request):
    return render(request, 'base.html')


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
    return render(request, 'profile.html', {'profile': profile})


def edit_profile(request):
    profile = WebUser.objects.get_or_create(user=request.user)[0]
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            
            # Add success notification
            messages.success(request, 'Profile updated successfully!')

            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'edit_profile.html', {'form': form})




@login_required
@permission_required('tournament.add_tournament', raise_exception=True)
def can_add_tournament(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST, request.FILES)
        if form.is_valid():
            tournament = form.save(commit=False)
            tournament.creator = request.user
            if 'img_url' in request.FILES:
                image_file = request.FILES['img_url']
                upload_result = cloudinary.uploader.upload(image_file)
                tournament.img_url = upload_result['secure_url']
            tournament.save()
            
            # Add success notification
            messages.success(request, 'Tournament added successfully!')

            return redirect('tournament_detail', pk=tournament.pk)
        else:
            # Add error notification if form is not valid
            messages.error(request, 'Error occurred while adding tournament. Please check the form and try again.')
    else:
        form = TournamentForm()
    return render(request, 'tournament/add_tournament.html', {'form': form})


@login_required
def can_edit_tournament(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    if tournament.creator != request.user:
        return HttpResponseForbidden("You do not have permission to edit this tournament.")
    
    if request.method == 'POST':
        form = TournamentForm(request.POST, request.FILES, instance=tournament)
        if form.is_valid():
            if 'img_url' in request.FILES:
                image_file = request.FILES['img_url']
                upload_result = cloudinary.uploader.upload(image_file)
                tournament.img_url = upload_result['secure_url']
            form.save()
            
            # Add success notification
            messages.success(request, 'Tournament updated!')

            return redirect('tournament_detail', pk=tournament.pk)
    else:
        form = TournamentForm(instance=tournament)
    
    return render(request, 'tournament/edit_tournament.html', {'form': form})


@login_required
def can_delete_tournament(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    if tournament.creator != request.user:
        return HttpResponseForbidden("You do not have permission to delete this tournament.")
    
    if request.method == 'POST':
        tournament.delete()
        
        # Add success notification
        messages.success(request, 'Tournament deleted!')

        return redirect('tournaments')
        # Redirect to a suitable page after deletion
    
    return render(request, 'tournament/delete_tournament.html', {'tournament': tournament})


@login_required
@permission_required('tournament.add_new', raise_exception=True)
def can_add_new(request):
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.creator = request.user
            if 'img_url' in request.FILES:
                image_file = request.FILES['img_url']
                upload_result = cloudinary.uploader.upload(image_file)
                new.img_url = upload_result['secure_url']
            new.save()
            
            # Add success notification
            messages.success(request, 'News added successfully!')

            return redirect('new_detail', pk=new.pk)
    else:
        form = NewForm()
    
    return render(request, 'tournament/add_new.html', {'form': form})


@login_required
def can_edit_new(request, pk):
    new = get_object_or_404(New, pk=pk)
    if new.creator != request.user:
        return HttpResponseForbidden("You do not have permission to edit this new.")
    
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES, instance=new)
        if form.is_valid():
            if 'img_url' in request.FILES:
                image_file = request.FILES['img_url']
                upload_result = cloudinary.uploader.upload(image_file)
                new.img_url = upload_result['secure_url']
            form.save()
            
            # Add success notification
            messages.success(request, 'News updated successfully!')

            return redirect('new_detail', pk=new.pk)
    else:
        form = NewForm(instance=new)
    
    return render(request, 'tournament/edit_new.html', {'form': form})


@login_required
def can_delete_new(request, pk):
    new = get_object_or_404(New, pk=pk)
    if new.creator != request.user:
        return HttpResponseForbidden("You do not have permission to delete this new.")
    
    if request.method == 'POST':
        new.delete()
        
        # Add success notification
        messages.success(request, 'News deleted successfully!')

        return redirect('home')
        # Redirect to a suitable page after deletion
    
    return render(request, 'tournament/delete_new.html', {'new': new})
