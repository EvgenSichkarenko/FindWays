from django import forms
from .models import City


class CityForm(forms.ModelForm):
    name = forms.CharField(label='City name', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    travel_time = forms.IntegerField(label='', widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    from_city = forms.ModelChoiceField(label='', queryset=City.objects.all(), widget=forms.Select(attrs={
         'class': 'form-control'
    }))
    to_city = forms.ModelChoiceField(label='', queryset=City.objects.all(), widget=forms.Select(attrs={
         'class': 'form-control'
    }))

    class Meta:
        model = City
        fields = ['name']
