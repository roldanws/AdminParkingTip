from django import forms
from .models import Event

from bootstrap_datepicker_plus import DatePickerInput
from bootstrap_datepicker_plus import TimePickerInput
from bootstrap_datepicker_plus import DateTimePickerInput
from bootstrap_datepicker_plus import MonthPickerInput
from bootstrap_datepicker_plus import YearPickerInput


class CustomForm(forms.Form):
    # name = forms.CharField(label="Name")
    date = forms.DateField(label="Date", widget=DatePickerInput())
    message = forms.CharField(label="Message", widget=forms.Textarea)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'start_date', 'end_date',
            
        ]
        widgets = {
            'start_date': DatePickerInput(options={'format': 'YYYY-MM-DD', 'debug': True}).start_of('event active days'),
            'end_date': DatePickerInput(options={'format': 'MM/DD/YYYY'}).end_of('event active days'),
            
        }
