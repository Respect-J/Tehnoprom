from rest_framework import serializers
from .models import PremiumPlan, UserPremiumSubscription


class PremiumPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumPlan
        fields = [
            'id',
            'name',
            'duration_in_days',
            'price',
            'discount_percentage',
            'discount_limit'
        ]


class UserPremiumSubscriptionSerializer(serializers.ModelSerializer):
    # Отображаем данные о плане в ответе
    plan = serializers.SerializerMethodField(read_only=True)
    plan_id = serializers.PrimaryKeyRelatedField(
        queryset=PremiumPlan.objects.all(),
        source='plan',
        write_only=True
    )

    class Meta:
        model = UserPremiumSubscription
        fields = [
            'id',
            'plan',
            'plan_id',
            'start_date',
            'end_date',
            'is_active',
        ]
        read_only_fields = ['start_date', 'end_date', 'is_active']

    def get_plan(self, obj):
        return PremiumPlanSerializer(obj.plan).data

    def create(self, validated_data):
        return UserPremiumSubscription.objects.create(**validated_data)

