from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import MyTokenObtainPairView, UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path("", UserListCreateView.as_view(), name="user-list-create"),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("<pk>/", UserRetrieveUpdateDestroyView.as_view(), name="user-retrieve-update-destroy"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
