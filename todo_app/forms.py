from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = Task
        fields = ('text',)
    
    def clean_text(self):
        data = self.cleaned_data["text"]
        texts = [s.text for s in Task.objects.all()]
        if data.title() in texts:
            raise forms.ValidationError("already present")
        else:
            return data
    
