from django.contrib import admin
from prediction.models import Prediction


class PredictionAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'price', 'location', 'update_date', 'is_active']
    search_fields = ['user', 'price', 'location']
    list_filter = ['update_date', 'is_active']

admin.site.register(Prediction, PredictionAdmin)