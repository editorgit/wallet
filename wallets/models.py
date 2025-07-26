from decimal import Decimal

from django.db import models
from rest_framework.exceptions import ValidationError


class Wallet(models.Model):
    label = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.label} ({self.balance})"


class Transaction(models.Model):
    wallet = models.ForeignKey(
        Wallet, related_name="transactions", on_delete=models.CASCADE
    )
    txid = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        new_balance = self.wallet.balance + self.amount
        if new_balance < Decimal("0.00"):
            raise ValidationError({"detail": "Wallet balance cannot be negative"})

    def save(self, *args, **kwargs):
        self.full_clean()
        self.wallet.balance += self.amount
        super().save(*args, **kwargs)
        self.wallet.save()
