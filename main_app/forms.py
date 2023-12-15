from django.forms import ModelForm
from .models import Concert

class ConcertForm(ModelForm):
    class Meta: 
        model = Concert
        fields = ['date', 'city']