from django.forms import ModelForm
from django import forms
from prediction.models import PredictionOffer, Prediction


class PredictionOfferForm(ModelForm):
    class Meta:
        model = PredictionOffer
        fields = ['user', 'prediction', 'phone']
        labels = {'phone': 'Phone'}
        widgets = {
            'user': forms.HiddenInput(),
            'prediction': forms.HiddenInput(),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone number...'})
        }

class PredictionCreateForm(ModelForm):
    class Meta:
        model = Prediction
        fields = ['user', 'image', 'title', 'description', 'price', 'location', 'is_active']
        widgets = {
            'user': forms.HiddenInput(),
        }
