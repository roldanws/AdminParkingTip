from django import forms
from django.forms import ModelForm

from .models import Corte


class DateInput(forms.DateInput):
    input_type = 'date'


class CorteForm(ModelForm):

    class Meta:
        model = Corte
        fields = ['created']
        widgets = {
            'created': DateInput(),
        }