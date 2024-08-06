from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from products.api.permissions import IsAdminOrReadOnly
from products.models import Product,Stock
from products.api.serializer import StockSerializer
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdminOrReadOnly]
# Create your views here.
# def product_list(request):
#     stocks=Stock.objects.all()
#     serializer=StockSerializer(stocks,many=True) ##stocks_list=list(stocks.values())
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['GET','PUT','DELETE','POST'])
# def stock_detail_list(request,id):
#     try:
#         stock=Stock.objects.get(pk=id)
#     except Stock.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer=StockSerializer(stock)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer=StockSerializer(stock,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         stock.delete()
#         return Response(status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer=StockSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)