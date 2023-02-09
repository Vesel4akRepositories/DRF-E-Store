from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ProductCategoryViewSet, ProductViewSet
from django.conf import settings
from django.conf.urls.static import static


app_name = 'products'

router = DefaultRouter()
router.register(r'categories', ProductCategoryViewSet)
#router.register(r'categories/<int:category_id>/', ProductViewSet.as_view({'get': 'retrieve_products_by_category'})),
router.register(r'', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('category/<int:category_id>/',  ProductViewSet.as_view({'get': 'retrieve_products_by_category'})),
]
