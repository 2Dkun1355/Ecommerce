from django.urls import path
from prediction.views import PredictionListViews, PredictionDetailView, PredictionOfferCreateView

urlpatterns = [
    path('catalog/', PredictionListViews.as_view(), name='catalog'),
    path('catalog/<pk>/', PredictionDetailView.as_view(), name='prediction_detail'),
    path('create/', PredictionOfferCreateView.as_view(), name='prediction_create'),

]