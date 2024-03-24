from django import forms
from .models import WebUser, Tournament, New
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class ProfileForm(forms.ModelForm):
    class Meta:
        model = WebUser
        fields = ['first_name','last_name','description', 'category']
    

class TournamentForm(forms.ModelForm):  
    class Meta:
        model = Tournament
        fields = ['name', 'start_date','end_date','location', 'surface', 'sponsor', 'entry_fee', 'prize_money', 'category','description', 'max_participants','img_url','phone_number','email']
        widgets = {
            'start_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'end_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'description': forms.TextInput(attrs={'placeholder': 'Max. characters 400'}),
            
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        entry_fee = cleaned_data.get('entry_fee')
        prize_money = cleaned_data.get('prize_money')
        max_participants = cleaned_data.get('max_participants')

        # Check if start date is after end date
        if start_date and end_date and start_date > end_date:
            self.add_error('start_date', forms.ValidationError("Start date cannot be after end date."))

        # Check if entry fee is negative
        if entry_fee is not None and entry_fee < 0:
            self.add_error('entry_fee', forms.ValidationError("Entry fee cannot be negative."))

        # Check if prize money is negative
        if prize_money is not None and prize_money < 0:
            self.add_error('prize_money', forms.ValidationError("Prize money cannot be negative."))
        
        if max_participants is not None and max_participants < 4:
            self.add_error('max_participants', forms.ValidationError("It is required a minimum of 4 players for this tournament."))

        return cleaned_data

class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ['title', 'content','img_url']