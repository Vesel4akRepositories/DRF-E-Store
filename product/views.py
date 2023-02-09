from rest_framework import permissions, viewsets
from rest_framework.response import Response
from .models import Product, ProductCategory
from .serializers import ProductSerializer, ProductCategorySerializer
from django.shortcuts import get_object_or_404

class ProductCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List and Retrieve product categories
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = (permissions.AllowAny, )


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List and Retrieve products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny, )

    def retrieve_products_by_category(self, request, category_id):
        category = get_object_or_404(ProductCategory, id=category_id)
        products = self.queryset.filter(category=category)
        serializer = self.serializer_class(products, many=True,context={'request': request})
        return Response(serializer.data)
