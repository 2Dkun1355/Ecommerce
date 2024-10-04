from django.forms import ModelForm
from django import forms
from prediction.models import PredictionOffer, Prediction


class PredictionOfferForm(ModelForm):
    class Meta:
        model = PredictionOffer
        fields = ['user', 'prediction', 'phone']
        widgets = {
            'user': forms.HiddenInput(),
            'prediction': forms.HiddenInput(),
            'phone': forms.TextInput(attrs={'class': "form-control bg-white"})
        }

class PredictionForm(ModelForm):
    class Meta:
        model = Prediction
        fields = ['user', 'image', 'title', 'description', 'price', 'location', 'is_active']
        widgets = {
            'user': forms.HiddenInput(),
            'image': forms.FileInput(attrs={'class': "form-control-file d-none", 'id': "file-upload", 'name': "file"}),
            'title': forms.TextInput(attrs={'class': "form-control bg-white"}),
            'description': forms.Textarea(attrs={'class': "form-control bg-white"}),
            'price': forms.TextInput(attrs={'class': "form-control bg-white"}),
            'location': forms.TextInput(attrs={'class': "form-control bg-white"}),
            'is_active': forms.CheckboxInput(attrs={'class': "form-check-input"})
        }
