from django.urls import path
from .views import RegionStatisticsAPIView
from .views import BehavioralAnalyticsView
from .views import UserTrendsAnalyticsView, UserActivityPredictionView

urlpatterns = [
    path('region/<str:region_name>/', RegionStatisticsAPIView.as_view(), name='region_statistics'),
    path('behavioral/', BehavioralAnalyticsView.as_view(), name='behavioral-analytics'),
    path('trends/', UserTrendsAnalyticsView.as_view(), name='user-trends'),
    path('predictions/', UserActivityPredictionView.as_view(), name='user-predictions'),
]
