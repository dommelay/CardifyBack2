from django import forms
from .models import Card, Deck

class CardForm(forms.ModelForm):
    deck = forms.ModelChoiceField(queryset=Deck.objects.all())

    class Meta:
        model = Card
        fields = ['id', 'deck', 'question', 'answer', 'image']