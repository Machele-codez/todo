from .models import Task
from django import forms
from django.http import request
import datetime, pytz

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    due_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    class Meta:
        model = Task
        fields = ('text', 'priority') #'due_date', 'due_time', 'due_datetime')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['due_datetime'].widget.attrs['placeholder'] = 'dd/mm/yy hrs:mins'
        # print(self.fields['due_datetime'].initial)

    def clean_due_datetime(self):
        input_due_datetime = self.cleaned_data['due_datetime']
        print("initial_due_datetime:".upper(),self.fields['due_datetime'].initial)
        print("input_due_datetime:".upper(),input_due_datetime)
        print(self.fields['due_datetime'].initial == input_due_datetime)
        if self.fields['due_datetime'].initial == input_due_datetime:
            raise forms.ValidationError(
                'please input a date',
                'no_date_input'
            )

        return input_due_datetime
