from typing import ClassVar

from rest_framework import generics

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.order_by("name")
    serializer_class = CategorySerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.select_related("category").filter(is_active=True).order_by("name")
    serializer_class = ProductSerializer
    filterset_fields: ClassVar = ["category"]
