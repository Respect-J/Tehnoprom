from pyclick.models import ClickTransaction
from pyclick.views import PyClickMerchantAPIView, TransactionCheck

from apps.orders.models import Order
from tg import send_message


class TransactionCheckCustomView(TransactionCheck):
    @classmethod
    def successfully_payment(cls, transaction: ClickTransaction):
        order = Order.objects.filter(pk=transaction.id).first()
        order.is_paid = True
        order.save()
        try:
            send_message(order)
        except Exception as e:
            print(f"Failed to send telegram message to group. err: {e}")
        print(f"perform_transaction for order_id: {transaction.id}, response: {transaction.action}")


class ClickTransactionTestView(PyClickMerchantAPIView):
    VALIDATE_CLASS = TransactionCheckCustomView
