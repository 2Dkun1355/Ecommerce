from audioop import reverse

from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from prediction.forms import PredictionOfferForm, PredictionCreateForm
from prediction.models import Prediction


class PredictionListViews(ListView):
    model = Prediction
    template_name = 'catalog.html'
    context_object_name = 'predictions'

class PredictionDetailViews(DetailView):
    model = Prediction
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        form = PredictionOfferForm()

        form.fields['prediction'].initial = self.get_object()
        form.fields['user'].initial = self.request.user if not self.request.user.is_anonymous else None

        context_data['form'] = form
        return context_data


class PredictionOfferCreateViews(CreateView):
    form_class = PredictionOfferForm
    success_url = reverse_lazy('catalog')


class PredictionCreateViews(CreateView):
    form_class = PredictionCreateForm
    success_url = reverse_lazy('catalog')
    template_name = 'create_prediction.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        form = PredictionCreateForm()

        form.fields['user'].initial = self.request.user

        context_data['form'] = form
        return context_data


class UserPredictionListViews(ListView):
    model = Prediction
    template_name = 'dashboard.html'
    context_object_name = 'predictions'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Prediction.objects.filter(user=user)

