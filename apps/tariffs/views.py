from rest_framework import generics, permissions
from .models import PremiumPlan, UserPremiumSubscription, UserModel
from .serializers import PremiumPlanSerializer, UserPremiumSubscriptionSerializer
from django.utils import timezone

class PremiumPlanListAPIView(generics.ListAPIView):

    queryset = PremiumPlan.objects.all()
    serializer_class = PremiumPlanSerializer
    permission_classes = [permissions.AllowAny]


class CreateSubscriptionAPIView(generics.CreateAPIView):
    queryset = UserPremiumSubscription.objects.all()
    serializer_class = UserPremiumSubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        plan = serializer.validated_data['plan']
        start_date = timezone.now()
        end_date = start_date + timezone.timedelta(days=plan.duration_in_days)


        subscription = serializer.save(
            user=UserModel.objects.get(id=self.request.user.id),
            start_date=start_date,
            end_date=end_date,
            is_active=True
        )


        user = UserModel.objects.get(id=self.request.user.id)
        if not user.is_premium:
            user.is_premium = True
            user.premium_end_date = end_date
        else:
            if user.premium_end_date and user.premium_end_date < end_date:
                user.premium_end_date = end_date
        user.save()


class MySubscriptionsAPIView(generics.ListAPIView):

    serializer_class = UserPremiumSubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserPremiumSubscription.objects.filter(user=self.request.user)
