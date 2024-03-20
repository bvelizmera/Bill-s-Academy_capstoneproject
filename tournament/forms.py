from django import forms
from .models import WebUser

class ProfileForm(forms.ModelForm):
    class Meta:
        model = WebUser
        fields = ['f_name','l_name','description']