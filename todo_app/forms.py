from .models import Item
from django import forms

class ItemForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = Item
        fields = '__all__'
    
    def clean_text(self):
        data = self.cleaned_data["text"]
        texts = [s.text for s in Item.objects.all()]
        if data.title() in texts:
            raise forms.ValidationError("already present")
        else:
            print(texts)
            return data
    
