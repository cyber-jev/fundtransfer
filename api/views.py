from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from users.models import User
from .serializers import UserSerializer
from decimal import Decimal


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        if User.objects.filter(phone_number=phone_number).exists():
            return Response(
                {"error": "Phone number already in use"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().create(request, *args, **kwargs)


class FundUserView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        # user = User.objects.get(phone_number=request.data.get("phone_number"))
        phone_number = request.data.get("phone_number")
        amount = request.data.get("amount")
        try:
            user = User.objects.get(phone_number=request.data.get("phone_number"))
            user.balance += Decimal(amount)
            user.save()
            return Response(
                {"status": "Account funded successfully"}, status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # if user:
        #     user.balance += Decimal(amount)
        #     user.save()
        #     return Response({"status": "Account funded successfully"}, status=status.HTTP_200_OK)
        # return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
