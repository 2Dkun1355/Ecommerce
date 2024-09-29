from django.contrib import admin
from prediction.models import Prediction, PredictionOffer


class PredictionAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'price', 'location', 'published_date', 'update_date', 'is_active']
    search_fields = ['user', 'price', 'location']
    list_filter = ['published_date', 'update_date', 'is_active']

class PredictionOfferAdmin(admin.ModelAdmin):
    list_display = ['user', 'prediction', 'phone', 'offer_date']
    search_fields = ['user', 'prediction', 'phone']
    list_filter = ['offer_date']


admin.site.register(Prediction, PredictionAdmin)
admin.site.register(PredictionOffer, PredictionOfferAdmin)
