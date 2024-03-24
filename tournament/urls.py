from . import views
from django.urls import path

urlpatterns = [
    #Tournament and News List pages
    path('tournaments/', views.TournamentList.as_view(), name='tournaments'),
    path('', views.NewsList.as_view(), name='home'),
    #Tournament Urls edition, addition, deletion
    path('tournament/<int:pk>/', views.tournament_detail, name='tournament_detail'),#details of each tournament
    path('add_tournament/', views.can_add_tournament, name='add_tournament'),#add tournament
    path('tournament/edit/<int:pk>', views.can_edit_tournament, name='edit_tournament'), #edit tournament
    path('tournament/delete/<int:pk>', views.can_delete_tournament, name='delete_tournament'), #delet tournament
    path('new/<int:pk>/', views.new_detail, name="new_detail"),#details of each new
    path('add_new/', views.can_add_new, name="add_new"),#add new
    path('new/edit/<int:pk>', views.can_edit_new, name='edit_new'),#edit new
    path('new/delete/<int:pk>', views.can_delete_new, name='delete_new'),#delete_new
]