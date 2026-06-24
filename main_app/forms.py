from django import forms
from .models import Release

class ReleaseForm(forms.ModelForm):
    class Meta:
        model = Release
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select Date Released',
                    'type': 'date'
                }
            )
        }