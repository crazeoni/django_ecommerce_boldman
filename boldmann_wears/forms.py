from django import forms
from .models import Bolducts

class BolductsForm(forms.ModelForm):
    show_boots = forms.BooleanField()

    class Meta:
        model = Bolducts
        fields = ['show_boots']
        labels = {'show_boots': 'boots'}
