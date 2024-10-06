from django.urls import path
from prediction.views import PredictionListViews, PredictionDetailViews, PredictionOfferCreateViews, \
    PredictionCreateViews, PredictionUpdateViews, PredictionDeleteViews, PredictionOfferDeleteViews

urlpatterns = [
    path('catalog/', PredictionListViews.as_view(), name='catalog'),
    path('detail/<pk>/', PredictionDetailViews.as_view(), name='detail'),
    path('update/<pk>/', PredictionUpdateViews.as_view(), name='prediction_update'),
    path('delete/<pk>/', PredictionDeleteViews.as_view(), name='prediction_delete'),
    path('create/', PredictionCreateViews.as_view(), name='prediction_create'),
    path('offer/create/', PredictionOfferCreateViews.as_view(), name='offer_create'),
    path('offer/delete/<pk>/', PredictionOfferDeleteViews.as_view(), name='offer_delete'),
]
