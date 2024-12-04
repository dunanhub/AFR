from django.contrib import admin
from django.urls import path, include
from auth_app.views import LoginView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('auth_app.urls')),  # Подключение auth_app
    path('api/login/', LoginView.as_view(), name='login'),
    path('', include('crm.urls')),
    path('api/analytics/', include('demographic_analytics.urls')),
]
