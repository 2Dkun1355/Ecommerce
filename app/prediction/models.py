from django.db import models
from django.contrib.auth.models import User
from enum import Enum


class LocationChoices(str, Enum):
    Lviv = 'Львів'
    Busk = 'Буськ'
    Toporiv = 'Топорів'

    @classmethod
    def choices(cls):
        res = tuple([(e.value, e.value) for e in cls])
        return res



class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/prediction/', null=True, blank=True)
    title = models.CharField(max_length=160)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=60, null=True, blank=True, choices=LocationChoices.choices())
    published_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("prediction_detail", kwargs={"pk": self.pk})

class PredictionOffer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    prediction = models.ForeignKey(Prediction, on_delete=models.CASCADE)
    phone = models.CharField(max_length=32)
    offer_date = models.DateField(auto_now_add=True)
