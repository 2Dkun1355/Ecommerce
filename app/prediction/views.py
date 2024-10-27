from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from prediction.forms import PredictionOfferForm, PredictionForm
from prediction.models import Prediction, PredictionOffer, PredictionCategory
from prediction.utils import creation_prediction


class PredictionListViews(ListView):
    model = Prediction
    paginate_by = 9
    template_name = 'prediction/catalog.html'
    context_object_name = 'predictions'
    # creation_prediction()

    def get_queryset(self):
        queryset = Prediction.objects.filter(is_active=True)
        category_slug = self.request.GET.get('category')
        location = self.request.GET.get('location')

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        if location:
            queryset = queryset.filter(location=location)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = PredictionCategory.objects.annotate(count=Count('prediction'))
        context['prediction'] = Prediction.objects.all()
        context['locations'] = Prediction.objects.values('location').annotate(count=Count('id'))
        return context


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
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        form = self.get_form()

        form.fields['view'] = "{% url 'prediction_update' %}"

        context_data['form'] = form
        return context_data

class PredictionDeleteViews(DeleteView):
    model = Prediction
    success_url = reverse_lazy('dashboard')

    def get(self, request, *arge, **kwargs):
        return self.delete(request, *arge, **kwargs)


class PredictionOfferCreateViews(CreateView):
    form_class = PredictionOfferForm
    success_url = reverse_lazy('catalog')

class PredictionOfferDeleteViews(DeleteView):
    model = PredictionOffer
    success_url = reverse_lazy('dashboard_my_feedback')

    def get(self, request, *arge, **kwargs):
        return self.delete(request, *arge, **kwargs)