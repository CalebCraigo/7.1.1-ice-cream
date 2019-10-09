from django.db import models
from django.utils import timezone
from django.urls import reverse

class Icecream(models.Model):

    AVAILABLE_CHOICES = [
    ('WEEKLY', 'Weekly'),
    ('DAILY', 'Daily'),
    ('SEASONAL', 'Seasonal'),
    ]

    BASE_CHOICES = [
    ('CHOCOLATE', 'Chocolate'),
    ('VANILLA', 'Vanilla'),
    ('STRAWBERRY', 'Strawberry'),
    ]

    flavor = models.CharField(max_length=255, default='')
    base = models.CharField(max_length=255, choices=BASE_CHOICES, default='VANILLA')
    available = models.CharField(max_length=255, choices=AVAILABLE_CHOICES, default='DAILY')
    featured = models.BooleanField(default=False)
    date_churned = models.DateTimeField('Date Churned', default=timezone.now)

    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.flavor

    def get_absolute_url(self):
        return reverse('ice_cream:index')


# Create your models here.
