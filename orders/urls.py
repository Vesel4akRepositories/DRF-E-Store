from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet)

app_name = 'orders'

urlpatterns = [
    path('', include(router.urls)),
]