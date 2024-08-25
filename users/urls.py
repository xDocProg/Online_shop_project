from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

from .views import RegisterViewSet, ConfirmEmailView, ChangePasswordView, LoginView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterViewSet.as_view(), name='register'),
    path('confirm-email/', ConfirmEmailView.as_view(), name='confirm_email'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
]
