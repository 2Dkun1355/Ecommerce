from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from prediction.models import Prediction, PredictionOffer, UserModel


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ['id', 'user', 'title', 'category', 'price', 'location',
              'published_date', 'is_active']

class PredictionOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionOffer
        fields = ['id', 'user', 'prediction', 'phone', 'offer_date']

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", 'username', 'last_name', 'first_name', 'phone', 'date_joined']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'phone', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            phone=validated_data['phone'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user