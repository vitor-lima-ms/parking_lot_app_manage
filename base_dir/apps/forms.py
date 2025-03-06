from django import forms
from .models import Automobile

class AutomobileForm(forms.ModelForm):
    class Meta:
        model = Automobile
        fields = [
            'model',
            'automobile_plate'
        ]