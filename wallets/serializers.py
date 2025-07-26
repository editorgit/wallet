from rest_framework_json_api import serializers
from .models import Wallet, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "wallet", "txid", "amount"]


class WalletSerializer(serializers.ModelSerializer):
    transactions = serializers.ResourceRelatedField(
        many=True,
        read_only=True,
        related_link_view_name="wallet-transaction-list",
        related_link_url_kwarg="wallet_pk",
    )

    class Meta:
        model = Wallet
        fields = ["id", "label", "balance", "transactions"]
