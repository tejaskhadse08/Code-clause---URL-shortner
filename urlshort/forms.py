from .models import ShortUrl
from django import forms


class CreateNewShortURL(forms.ModelForm):
    class Meta:
        model = ShortUrl
        fields = {'long_url'}
        widgets = {
            'long_url': forms.TextInput(attrs={'class': 'from-control'})
        }
