from django.contrib import admin
from products.models import *
# Register your models here.
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['id','product', 'price', 'last_updated', 'stock']
    search_fields = ['product','in_stock']
    list_editable = ['price']
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']