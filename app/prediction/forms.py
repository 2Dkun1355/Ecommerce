from django import forms
from django.forms import ModelForm

from prediction.models import PredictionOffer


class PredictionOfferForm(ModelForm):
    class Meta:
        model = PredictionOffer
        fields = ['user', 'prediction', 'phone']
        labels = {'phone': 'Телефон'}
        widgets = {
            'user': forms.HiddenInput(),
            'prediction': forms.HiddenInput(),
            'phone': forms.TextInput(attrs={'placeholder': 'Введіть номер телефону...'}),
        }