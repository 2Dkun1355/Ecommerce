from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from prediction.forms import PredictionOfferForm
from prediction.models import Prediction


class PredictionListViews(ListView):
    model = Prediction
    template_name = 'catalog.html'
    context_object_name = 'predictions'

class PredictionDetailView(DetailView):
    model = Prediction
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        form = PredictionOfferForm()

        form.fields['prediction'].initial = self.get_object()

        if not self.request.user.is_anonymous:
            form.fields['user'].initial = self.request.user

        context_data['form'] = form
        return context_data


class PredictionOfferCreateView(CreateView):
    form_class = PredictionOfferForm
    success_url = reverse_lazy('catalog')