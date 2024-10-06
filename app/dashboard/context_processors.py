from prediction.models import Prediction, PredictionOffer


def dashboard_context(request):
    if request.user.is_authenticated:
        return {
        'prediction': Prediction.objects.filter(user=request.user).count(),
        'my_feedback': PredictionOffer.objects.filter(user=request.user).count(),
        'user_feedback': PredictionOffer.objects.filter(prediction__user=request.user).count(),
        }
    else:
        return {}