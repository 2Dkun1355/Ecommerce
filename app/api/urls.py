from rest_framework.routers import DefaultRouter
from api.views import PredictionViewSet, PredictionOfferViewSet, UserViewSet

router = DefaultRouter()
router.register('prediction', PredictionViewSet, basename='prediction'),
router.register('offer', PredictionOfferViewSet, basename='offer'),
router.register('user', UserViewSet, basename='user'),
urlpatterns = router.urls