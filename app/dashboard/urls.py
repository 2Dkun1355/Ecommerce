from django.urls import path

from dashboard.views import UserPredictionListViews

urlpatterns = [
    path('', UserPredictionListViews.as_view(), name='dashboard'),
]