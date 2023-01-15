
from django.urls import path, include

from .views import ListCart, DetailCart, RegistrationAPIView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'core'

urlpatterns = [
   path('carts', ListCart.as_view(), name='allcarts'),
   path('carts/<int:pk>', DetailCart.as_view(), name='cartdetail'),
   path('auth/register/', RegistrationAPIView.as_view(), name='register'),
   path('auth/login/', TokenObtainPairView.as_view(), name='login'),
   path('auth/refresh-token', TokenRefreshView.as_view(), name='refreshtoken'),
   path(r'profile/(?P<user_id>\w+)$', UserProfileView.as_view(), name='profile'),
]
