from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Cart
from .serializers import CartSerializer, RegistrationSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import uuid
from django.contrib.auth import get_user_model

class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        # serializer.is_valid(raise_exception = True)
        # serializer.save()
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "Пользователь создан успешно",
                
                "User": serializer.data}, status=status.HTTP_201_CREATED
                )
        
        return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListCart(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer    