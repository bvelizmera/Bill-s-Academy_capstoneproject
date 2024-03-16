from . import views
from django.urls import path

urlpatterns = [
    path('tournaments/', views.TournamentList.as_view(), name='tournaments'),
    path('', views.NewsList.as_view(), name='home')
]