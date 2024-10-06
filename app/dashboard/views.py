from django.urls import reverse_lazy

from prediction.models import Prediction, PredictionOffer
from django.views.generic import ListView, DetailView, CreateView, DeleteView


class DashboardListViews(ListView):
    model = Prediction
    paginate_by = 5
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'predictions'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Prediction.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'dashboard'
        return context

class DashboardMyFeedbackViews(ListView):
    model = PredictionOffer
    paginate_by = 5
    template_name = 'dashboard/dashboard_my_feedback.html'
    context_object_name = 'offers'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return PredictionOffer.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'my_feedback'
        return context

class DashboardUserFeedbackViews(ListView):
    model = PredictionOffer
    paginate_by = 5
    template_name = 'dashboard/dashboard_user_feedback.html'
    context_object_name = 'offers'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return PredictionOffer.objects.filter(prediction__user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'user_feedback'
        return context
