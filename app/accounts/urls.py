from django.urls import path
from .views import SignUpView, UserProfileUpdateView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('profile/', UserProfileUpdateView.as_view(), name='user_profile'),
]