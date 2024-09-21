from django.contrib import admin
from prediction.models import Prediction


class PredictionAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'price', 'location', 'published_date', 'update_date', 'is_active']
    search_fields = ['user', 'price', 'location']
    list_filter = ['published_date', 'update_date', 'is_active']

admin.site.register(Prediction, PredictionAdmin)