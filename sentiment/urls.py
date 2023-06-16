from django.urls import path
from sentiment.views import AnalyseSentimentAPIView

app_name = "sentiment"

urlpatterns = [
    path('analyze', AnalyseSentimentAPIView.as_view(), name='analyze')
]
