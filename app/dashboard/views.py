from prediction.models import Prediction
from django.views.generic import ListView, DetailView, CreateView

class UserPredictionListViews(ListView):
    model = Prediction
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'predictions'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Prediction.objects.filter(user=user)

