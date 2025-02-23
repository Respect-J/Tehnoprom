from rest_framework import generics, permissions
from .models import Wallet
from .serializers import WalletSerializer


class UserWalletView(generics.ListAPIView):

    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        return Wallet.objects.filter(user=self.request.user.id)
