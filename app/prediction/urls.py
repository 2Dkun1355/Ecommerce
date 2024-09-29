from django.urls import path
from prediction.views import PredictionListViews, PredictionDetailViews, PredictionOfferCreateViews, \
    UserPredictionListViews, PredictionCreateViews

urlpatterns = [
    path('catalog/', PredictionListViews.as_view(), name='catalog'),
    path('catalog/<pk>/', PredictionDetailViews.as_view(), name='detail'),
    path('create/', PredictionOfferCreateViews.as_view(), name='create_offer'),
    path('dashboard/', UserPredictionListViews.as_view(), name='dashboard'),
    path('create_prediction/', PredictionCreateViews.as_view(), name='create_prediction')
]