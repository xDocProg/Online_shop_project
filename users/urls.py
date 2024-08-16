from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterViewSet, ConfirmEmailView, LoginView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterViewSet.as_view(), name='register'),
    path('confirm-email/', ConfirmEmailView.as_view(), name='confirm_email'),
    path('login/', LoginView.as_view(), name='login'),

    # JWT-аутентификация
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
