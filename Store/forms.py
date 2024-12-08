from django import forms
from .models import Subscribers

# Creating the Subscribers Form

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers # Model name
        fields = ['email']  # Fields to be shown in the form



