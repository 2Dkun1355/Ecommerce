from django.urls import path

from dashboard.views import DashboardListViews, DashboardOfferListViews

urlpatterns = [
    path('', DashboardListViews.as_view(), name='dashboard'),
    path('offer/', DashboardOfferListViews.as_view(), name='dashboard_offer'),
]