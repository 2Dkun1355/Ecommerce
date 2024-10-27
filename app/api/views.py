from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status, filters
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from api.serialisers import PredictionSerializer, PredictionOfferSerializer, UserCreateSerializer, \
    UserListSerializer
from prediction.models import Prediction, PredictionOffer, UserModel


class PredictionViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description']
    filterset_fields = ['price', 'location', 'category']

class PredictionOfferViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = PredictionOffer.objects.all()
    serializer_class = PredictionOfferSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['user', 'phone']
    filterset_fields = ['user']

class UserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = UserModel.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserListSerializer