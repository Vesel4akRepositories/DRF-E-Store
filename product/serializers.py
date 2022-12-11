from rest_framework import serializers

from .models import ProductCategory, Product

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'   


#https://github.com/earthcomfy/django-ecommerce-api/blob/master/products/urls.py