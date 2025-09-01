from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Transaction
from .serializers import UserSerializer, TransactionSerializer, WalletUpdateSerializer
from drf_yasg.utils import swagger_auto_schema
from decimal import Decimal
from django.http import JsonResponse



def home(request):
    return JsonResponse({
        "message": "Welcome to Wallet API 🚀",
        "endpoints": ["/users/", "/wallet/update/", "/transactions/<user_id>/"],
        "docs": "/swagger/"
    })


@api_view(["GET"])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)




@swagger_auto_schema(method="post", request_body=WalletUpdateSerializer)
@api_view(['POST'])
def update_wallet(request):
    user_id = request.data.get('user_id')
    amount = request.data.get('amount')

    if user_id is None or amount is None:
        return Response({"error": "user_id and amount are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    try:
        amount = Decimal(amount)
    except ValueError:
        return Response({"error": "Invalid amount"}, status=status.HTTP_400_BAD_REQUEST)

    user.wallet_balance += amount
    user.save()

    Transaction.objects.create(user=user, amount=amount)

    return Response({"message": "Wallet updated", "wallet_balance": user.wallet_balance})

@api_view(["GET"])
def fetch_transactions(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error":"User Not Found"}, status=status.HTTP_404_NOT_FOUND)
    
    transactions = user.transactions.all().order_by('-timestamp')
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)