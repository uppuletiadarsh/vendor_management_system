from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, PurchaseOrderViewSet, HistoricalPerformanceViewSet, fetch_details

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)
router.register(r'historical_performance', HistoricalPerformanceViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/fetch-details/', fetch_details, name='fetch_details'),
]