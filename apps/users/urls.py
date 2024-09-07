from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    UserCreateView,
    MyTokenObtainPairView,
    VerifyPhoneView
)

urlpatterns = [

    path('register/', UserCreateView.as_view(), name='register'),
    path('verify-phone/', VerifyPhoneView.as_view(), name='verify-phone'),

    # JWT токены
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
