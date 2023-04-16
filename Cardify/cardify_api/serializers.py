from rest_framework import serializers
from .models import Deck
from .models import Card

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('id', 'title', 'subject', 'comments', 'topic', 'classs',)

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'question', 'answer', 'image','deck',)