from django.urls import path

from dashboard.views import DashboardListViews, DashboardMyFeedbackViews, DashboardUserFeedbackViews, \
    UserProfileUpdateView

urlpatterns = [
    path('', DashboardListViews.as_view(), name='dashboard'),
    path('user_profile/<str:username>/', UserProfileUpdateView.as_view(), name='user_profile'),
    path('offer/my_feedback/', DashboardMyFeedbackViews.as_view(), name='dashboard_my_feedback'),
    path('offer/user_feedback/', DashboardUserFeedbackViews.as_view(), name='dashboard_user_feedback'),
]