from django.views.generic import ListView
from prediction.models import Prediction


class PredictionListViews(ListView):
    model = Prediction
    template_name = 'catalog.html'
    context_object_name = 'predictions'