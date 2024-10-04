from audioop import reverse
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from prediction.forms import PredictionOfferForm, PredictionForm
from prediction.models import Prediction


class PredictionListViews(ListView):
    model = Prediction
    template_name = 'prediction/catalog.html'
    context_object_name = 'predictions'

    def get_queryset(self):
        return Prediction.objects.filter(is_active=True)


class PredictionDetailViews(DetailView):
    model = Prediction
    template_name = 'prediction/detail.html'

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
    form_class = PredictionForm
    template_name = 'prediction/create.html'
    success_url = reverse_lazy('catalog')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        form = self.get_form()

        form.fields['user'].initial = self.request.user
        form.fields['view'] = "{% url 'prediction_create' %}"

        context_data['form'] = form
        return context_data


class PredictionUpdateViews(UpdateView):
    model = Prediction
    form_class = PredictionForm
    template_name = 'prediction/create.html'
    success_url = reverse_lazy('detail')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        form = self.get_form()

        form.fields['view'] = "{% url 'prediction_update' %}"

        context_data['form'] = form
        return context_data


class PredictionDeleteViews(DeleteView):
    model = Prediction
    success_url = reverse_lazy('detail')