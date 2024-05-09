from rest_framework import viewsets
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class HistoricalPerformanceViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
from django.http import JsonResponse
from .models import Vendor, PurchaseOrder, HistoricalPerformance

def fetch_details(request):
    try:
        # Fetch details for vendors
        vendors = Vendor.objects.all()
        serialized_vendors = [{'name': vendor.name, 'contact_details': vendor.contact_details, 'address': vendor.address, 'vendor_code': vendor.vendor_code,
                               'on_time_delivery_rate': vendor.on_time_delivery_rate, 'quality_rating_avg': vendor.quality_rating_avg,
                               'average_response_time': vendor.average_response_time, 'fulfillment_rate': vendor.fulfillment_rate} for vendor in vendors]

        # Fetch details for purchase orders
        purchase_orders = PurchaseOrder.objects.all()
        serialized_purchase_orders = [{'vendor': order.vendor.name, 'po_number': order.po_number, 'order_date': order.order_date,
                                       'delivery_date': order.delivery_date, 'items': order.items, 'quantity': order.quantity,
                                       'status': order.status, 'quality_rating': order.quality_rating, 'issue_date': order.issue_date,
                                       'acknowledgment_date': order.acknowledgment_date} for order in purchase_orders]

        # Fetch details for historical performance
        historical_performances = HistoricalPerformance.objects.all()
        serialized_historical_performances = [{'vendor': performance.vendor.name, 'date': performance.date,
                                                'on_time_delivery_rate': performance.on_time_delivery_rate,
                                                'quality_rating_avg': performance.quality_rating_avg,
                                                'average_response_time': performance.average_response_time,
                                                'fulfillment_rate': performance.fulfillment_rate} for performance in historical_performances]

        # Combine serialized data into a dictionary
        serialized_data = {
            'vendors': serialized_vendors,
            'purchase_orders': serialized_purchase_orders,
            'historical_performances': serialized_historical_performances
        }

        # Return the serialized data as JSON response
        return JsonResponse(serialized_data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)