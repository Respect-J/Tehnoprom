from django.contrib import admin
from .models import PremiumPlan, UserPremiumSubscription


@admin.register(PremiumPlan)
class PremiumPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'duration_in_days', 'price', 'discount_percentage', 'discount_limit')
    search_fields = ('name',)
    list_filter = ('discount_percentage',)


@admin.register(UserPremiumSubscription)
class UserPremiumSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'plan', 'start_date', 'end_date', 'is_active')
    search_fields = ('user__username', 'plan__name')
    list_filter = ('is_active', 'plan', 'start_date', 'end_date')
