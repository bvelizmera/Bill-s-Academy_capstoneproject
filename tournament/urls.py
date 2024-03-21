from . import views
from django.urls import path

urlpatterns = [
    path('tournaments/', views.TournamentList.as_view(), name='tournaments'),
    path('', views.NewsList.as_view(), name='home'),
    path('tournament/<int:pk>/', views.tournament_detail, name='tournament_detail'),
    path('new/<int:pk>/', views.new_detail, name="new_detail"),
    path('add_tournament/', views.can_add_tournament, name='add_tournament'),
    path('tournament/edit/<int:pk>', views.can_edit_tournament, name='edit_tournament'),
    path('tournament/delete/<int:pk>', views.can_delete_tournament, name='delete_tournament'),
]