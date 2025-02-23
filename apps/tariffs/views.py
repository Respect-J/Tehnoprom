from rest_framework import generics, permissions
from .models import PremiumPlan, UserPremiumSubscription, UserModel
from .serializers import PremiumPlanSerializer, UserPremiumSubscriptionSerializer
from django.utils import timezone
from django.core.exceptions import ValidationError

from apps.wallets.models import Wallet, Transaction


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
        user = UserModel.objects.get(id=self.request.user.id)
        start_date = timezone.now()
        end_date = start_date + timezone.timedelta(days=plan.duration_in_days)

        # 1. Проверяем кошелёк пользователя
        try:
            wallet = Wallet.objects.get(user=user)
        except Wallet.DoesNotExist:
            raise ValidationError('Кошелёк не найден. Обратитесь в поддержку.')

        # 2. Проверяем баланс
        if wallet.balance < plan.price:
            raise ValidationError('Недостаточно средств на кошельке для покупки премиум-плана.')

        # 3. Списываем средства
        wallet.balance -= plan.price
        wallet.save()

        # 4. Создаём запись о транзакции
        Transaction.objects.create(
            wallet=wallet,
            amount=plan.price,
            transaction_type=Transaction.WITHDRAW,
            description=f"Покупка премиум-плана '{plan.name}'"
        )

        # 5. Создаём подписку
        subscription = serializer.save(
            user=UserModel.objects.get(id=user.id),
            start_date=start_date,
            end_date=end_date,
            is_active=True
        )


        if not user.is_premium:
            user.is_premium = True
            user.premium_end_date = end_date
        else:
            # Если у пользователя уже есть премиум, продлеваем при необходимости
            if user.premium_end_date and user.premium_end_date < end_date:
                user.premium_end_date = end_date
        user.save()


class MySubscriptionsAPIView(generics.ListAPIView):
    serializer_class = UserPremiumSubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserPremiumSubscription.objects.filter(user=self.request.user)
