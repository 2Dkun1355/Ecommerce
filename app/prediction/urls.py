from django.urls import path
from prediction.views import PredictionListViews, PredictionDetailView

urlpatterns = [
    path('catalog/', PredictionListViews.as_view()),
    path('catalog/<pk>/', PredictionDetailView.as_view(), name='detail')
]