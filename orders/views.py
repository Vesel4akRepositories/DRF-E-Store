from rest_framework import viewsets, status
from .models import Order, OrderProduct
from product.models import Product
from .serializers import OrderSerializer
from rest_framework.response import Response
import json

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        print(self.request.user.id)
        order_ids = OrderProduct.objects.filter(order__customer=self.request.user.id).values_list('order', flat=True)
        return self.queryset.filter(id__in=order_ids)
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['customer'] = self.request.user
        
        order = serializer.save()
    
        products = json.loads(request.data.get('products', '[]'))
        for product_data in products:
            product = Product.objects.get(id=int(product_data['id']))
            OrderProduct.objects.create(
                order=order,
                product=product,
                quantity=int(product_data['quantity']),
                price=product.price
            )
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

