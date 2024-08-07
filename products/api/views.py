from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from products.api.permissions import IsSuperUserOrReadWrite
from products.models import Product,Stock
from products.api.serializer import StockSerializer
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsSuperUserOrReadWrite]
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class =ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
