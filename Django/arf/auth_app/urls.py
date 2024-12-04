from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LoginView, UserProfileView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', UserProfileView.as_view(), name='user-profile'),
]
