from decimal import Decimal

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from wallets.models import Transaction, Wallet


class WalletTransactionTests(TestCase):

    def setUp(self):
        self.wallet = Wallet.objects.create(label="Test Wallet")

    def test_wallet_creation(self):
        self.assertEqual(self.wallet.balance, Decimal("0.00"))

    def test_add_positive_transaction(self):
        Transaction.objects.create(
            wallet=self.wallet, txid="tx1", amount=Decimal("100.00")
        )
        self.wallet.refresh_from_db()
        self.assertEqual(self.wallet.balance, Decimal("100.00"))

    def test_add_negative_transaction_within_balance(self):
        Transaction.objects.create(
            wallet=self.wallet, txid="tx2", amount=Decimal("100.00")
        )
        Transaction.objects.create(
            wallet=self.wallet, txid="tx3", amount=Decimal("-30.00")
        )
        self.wallet.refresh_from_db()
        self.assertEqual(self.wallet.balance, Decimal("70.00"))

    def test_reject_transaction_causing_negative_balance(self):
        with self.assertRaises(ValidationError):
            Transaction.objects.create(
                wallet=self.wallet, txid="tx4", amount=Decimal("-50.00")
            )
