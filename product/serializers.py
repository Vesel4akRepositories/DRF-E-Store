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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if request:
            representation['image'] = request.build_absolute_uri(representation['image'])
        return representation


#https://github.com/earthcomfy/django-ecommerce-api/blob/master/products/urls.py
#brew services stop postgresql  