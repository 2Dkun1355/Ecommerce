from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

UserModel = get_user_model()

class Prediction(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/prediction/', null=True, blank=True)
    title = models.CharField(max_length=160)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=60, null=True, blank=True)
    published_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey('PredictionCategory', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_detail_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('prediction_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('prediction_delete', kwargs={'pk': self.pk})


class PredictionOffer(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    prediction = models.ForeignKey(Prediction, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16)
    offer_date = models.DateField(auto_now_add=True)

    def get_delete_url(self):
        return reverse('offer_delete', kwargs={'pk': self.pk})

class PredictionCategory(models.Model):
    title = models.CharField(max_length=24, unique=True)
    slug = models.SlugField(max_length=24, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        self.slug = self.title.replace(' ', '_').lower()
        super().save(*args, **kwargs)