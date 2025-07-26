from rest_framework import viewsets, mixins
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['label', 'balance']
    ordering = ['label']


class TransactionViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = Transaction.objects.select_related('wallet').all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['wallet', 'txid', 'amount']
    ordering_fields = ['amount', 'created_at']
    ordering = ['-id']

