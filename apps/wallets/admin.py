from django.contrib import admin
from .models import Wallet, Transaction


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'balance', 'created_at')
    search_fields = ('user__username',)
    readonly_fields = ('created_at',)
    list_filter = ('created_at',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'wallet', 'transaction_type', 'amount', 'created_at', 'description')
    search_fields = ('wallet__user__username', 'description')
    list_filter = ('transaction_type', 'created_at')
    readonly_fields = ('created_at',)
