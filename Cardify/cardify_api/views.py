from django.shortcuts import render
from rest_framework import generics
from .serializers import DeckSerializer
from .serializers import CardSerializer
from .models import Card
from .models import Deck
from django.shortcuts import render, redirect 
from .forms import CardForm 

# Create your views here.
def create_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.deck = form.cleaned_data['deck']
            card.save()
            return redirect('card_detail', pk=card.pk)
    else: 
        form = CardForm()
    return render(request, 'create_card.html', {'form':form})
    

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

