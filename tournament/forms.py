from django import forms
from .models import WebUser, Tournament

class ProfileForm(forms.ModelForm):
    class Meta:
        model = WebUser
        fields = ['f_name','l_name','description', 'category']

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'start_date','end_date','location', 'surface', 'sponsor' , 'entry_fee', 'prize_money', 'category','description', 'max_participants']