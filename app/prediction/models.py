from django.db import models
from django.contrib.auth.models import User

class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/prediction/', null=True, blank=True)
    title = models.CharField(max_length=160)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=60, null=True, blank=True)
    published_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
