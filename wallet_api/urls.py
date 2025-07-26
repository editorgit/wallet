from django.contrib import admin
from django.urls import path, include

from rest_framework_json_api.exceptions import exception_handler
from rest_framework.settings import api_settings

from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from wallets.views import WalletViewSet, TransactionViewSet

# Основной router
router = DefaultRouter()
router.register(r'wallets', WalletViewSet, basename='wallet')
router.register(r'transactions', TransactionViewSet, basename='transaction')

wallets_router = NestedDefaultRouter(router, r'wallets', lookup='wallet')
wallets_router.register(r'transactions', TransactionViewSet, basename='wallet-transaction')

api_settings.EXCEPTION_HANDLER = exception_handler

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(wallets_router.urls)),
]
