from . import views
from django.urls import path

urlpatterns = [
    path('', views.TournamentList.as_view(), name='home'),
]