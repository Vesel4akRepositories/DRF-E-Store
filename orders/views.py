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
        return self.queryset.filter(customer=self.request.user)
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
    
        products = json.loads(request.data.get('products', '[]'))
        print(products)
        for product_data in products:
            print('jello')
            print(product_data)
            product = Product.objects.get(id=int(product_data['id']))
            OrderProduct.objects.create(
                order=order,
                product=product,
                quantity=int(product_data['quantity']),
                price=product.price
            )
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

