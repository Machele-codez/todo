from .models import Task
from django import forms
from django.http import request
from django.contrib.auth import get_user

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('text', 'priority')
    
    # def clean_text(self):
    #     data = self.cleaned_data["text"]
    #!     texts = [s.text for s in Task.objects.filter()]
    #     if data.title() in texts:   
    #         raise forms.ValidationError("already present")
    #     else:
    #         return data
    
