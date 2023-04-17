from django.db import models

# Create your models here.
SUBJECT_CHOICES = [
    ('Math', 'math'),
    ('Science', 'science'),
    ('Social Studies', 'social'),
    ('English', 'english'),
]

class Deck(models.Model):
    title = models.CharField()
    subject = models.CharField(choices=SUBJECT_CHOICES, default='math')
    topic = models.CharField()
    classs = models.CharField()
    comments = models.CharField()

class Card(models.Model):
    deck = models.ForeignKey(Deck, related_name='owner', null = True, on_delete = models.CASCADE)
    question = models.CharField()
    answer = models.CharField()
    image = models.CharField()
