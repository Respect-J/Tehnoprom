from rest_framework import serializers
from .models import Wallet, Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('id', 'wallet', 'amount', 'transaction_type', 'description', 'created_at')

    def create(self, validated_data):

        transaction = super().create(validated_data)
        wallet = transaction.wallet

        if transaction.transaction_type == Transaction.DEPOSIT:
            wallet.balance += transaction.amount
        elif transaction.transaction_type == Transaction.WITHDRAW:
            wallet.balance -= transaction.amount

        wallet.save()
        return transaction


class WalletSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    transactions = TransactionSerializer(many=True, read_only=True)

    class Meta:
        model = Wallet
        fields = ('id', 'user', 'balance', 'created_at', 'transactions')
        read_only_fields = ('balance',)
