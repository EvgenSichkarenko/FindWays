from django import forms
from .models import City


class RoutForm(forms.Form):
    from_city = forms.ModelChoiceField(label='', queryset=City.objects.all(), widget=forms.Select(attrs={
         'class': 'js-example-basic-single form-control'}))
    to_city = forms.ModelChoiceField(label='', queryset=City.objects.all(), widget=forms.Select(attrs={
         'class': 'form-control js-example-basic-single'
    }))
    cities = forms.ModelMultipleChoiceField(
        label='Throuth country',
        queryset=City.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control js-example-basic-multiple'
        })
    )
    travel_time = forms.IntegerField(label='', widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
