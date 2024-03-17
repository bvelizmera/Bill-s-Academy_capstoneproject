from . import views
from django.urls import path

urlpatterns = [
    path('tournaments/', views.TournamentList.as_view(), name='tournaments'),
    path('', views.NewsList.as_view(), name='home'),
    path('tournament/<int:pk>/', views.tournament_detail, name='tournament_detail'),
    path('new/<int:pk>/', views.new_detail, name="new_detail"),
]