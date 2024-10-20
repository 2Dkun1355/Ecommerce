from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from accounts.forms import CustomUserUpdateForm
from prediction.models import Prediction, PredictionOffer
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


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
            return PredictionOffer.objects.filter(prediction__user=user).select_related('user', 'prediction')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'user_feedback'
        return context

