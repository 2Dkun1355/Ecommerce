from django.urls import path
from prediction.views import PredictionListViews

urlpatterns = [
    path('category/', PredictionListViews.as_view())
]