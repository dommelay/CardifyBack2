from django.contrib import admin

# Register your models here.
from .models import Deck
from .models import Card
admin.site.register(Deck)
admin.site.register(Card)
