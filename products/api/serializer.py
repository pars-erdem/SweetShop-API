from rest_framework import serializers
from products.models import Product,Stock
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'