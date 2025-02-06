from django.urls import path
from .views import (
    PremiumPlanListAPIView,
    CreateSubscriptionAPIView,
    MySubscriptionsAPIView
)

urlpatterns = [
    path('premium-plans/', PremiumPlanListAPIView.as_view(), name='premium-plans-list'),
    path('subscribe/', CreateSubscriptionAPIView.as_view(), name='create-subscription'),
    path('my-subscriptions/', MySubscriptionsAPIView.as_view(), name='my-subscriptions'),
]
