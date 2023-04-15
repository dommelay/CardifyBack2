from django.shortcuts import render
from rest_framework import generics
from .serializers import DeckSerializer
from .serializers import CardSerializer
from .models import Card
from .models import Deck

# Create your views here.
class DeckList(generics.ListCreateAPIView):
    queryset = Deck.objects.all().order_by('id')
    serializer_class = DeckSerializer

class DeckDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deck.objects.all().order_by('id')
    serializer_class = DeckSerializer

class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all().order_by('id')
    serializer_class = CardSerializer

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all().order_by('id')
    serializer_class = CardSerializer

