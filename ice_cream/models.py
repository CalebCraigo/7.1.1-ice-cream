from django.db import models
from django.utils import timezone

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

    def __str__(self):
        return self.flavor

# class Option(models.Model):
#     options = models.ForeignKey(Icecream, on_delete=models.CASCADE)
#     choices_text = models.CharField(max_length=200)
#     featured = models.BooleanField(default= False)
#     pud_date = models.DateTimeField('Date Churned', default=timezone.now)
#
#     def __str__(self):
#         return self.choices_text


# Create your models here.
