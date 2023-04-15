from django.urls import path
from . import views

urlpatterns = [
    path('api/decks', views.DeckList.as_view(), name='deck_list'),
    path('api/decks/<int:pk>', views.DeckDetail.as_view(), name='deck_detail'),
    path('api/cards', views.CardList.as_view(), name='card_list'),
    path('api/cards/<int:pk>', views.CardDetail.as_view(), name='card_detail'),
]