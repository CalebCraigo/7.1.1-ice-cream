from django.db import models
from django.utils import timezone

class Icecream(models.Model):
    ice_cream_text = models.CharField(max_length=200)


    def __str__(self):
        return self.ice_cream_text

class Option(models.Model):
    options = models.ForeignKey(Icecream, on_delete=models.CASCADE)
    choices_text = models.CharField(max_length=255)
    featured = models.BooleanField(default= False)
    pud_date = models.DateTimeField('Date Churned', default=timezone.now)

    def __str__(self):
        return self.choices_text


# Create your models here.
