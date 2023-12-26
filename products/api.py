from rest_framework import generics
from .models import Product,Brand
from .serializers import ProductDetailserializer,ProductListSerializer
from .serializers import BrandDetailserializer,BrandListSerializer
from .pagination import Mypagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ProductListApi(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductListSerializer

    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['brand', 'flag']
    search_fields = ['name', 'subtitle']
    ordering_fields = ['price']

   

class ProductDetailApi(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductDetailserializer

class BrandListApi(generics.ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandListSerializer
    pagination_class=Mypagination


class BrandDetailApi(generics.RetrieveAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandDetailserializer

