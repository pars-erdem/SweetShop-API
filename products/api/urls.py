from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views as api_views
router = DefaultRouter()
router.register(r'stock', api_views.StockViewSet)
router.register(r'product', api_views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
