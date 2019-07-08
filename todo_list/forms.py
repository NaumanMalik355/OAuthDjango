from django import forms
from .models import List

class HomeForm(forms.ModelForm):
    # item=forms.CharField()
    # completed=forms.BooleanField()
    class Meta:
        model = List
        fields= ["item", "completed"]