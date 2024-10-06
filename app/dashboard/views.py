from django.urls import reverse_lazy

from prediction.models import Prediction, PredictionOffer
from django.views.generic import ListView, DetailView, CreateView, DeleteView


class DashboardListViews(ListView):
    model = Prediction
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'predictions'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Prediction.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            context['offers'] = PredictionOffer.objects.filter(user=user)
        return context

class DashboardOfferListViews(ListView):
    model = PredictionOffer
    template_name = 'dashboard/dashboard_my_offer.html'
    context_object_name = 'offers'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return PredictionOffer.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            context['predictions'] = Prediction.objects.filter(user=user)
        return context
