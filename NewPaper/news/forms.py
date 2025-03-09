from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'pub_date']
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'}),
        }