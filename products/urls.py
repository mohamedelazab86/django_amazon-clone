from django.urls import path
from .views import ProductList,ProductDetail,BrandDetail,BrandList
from .api import ProductListApi,ProductDetailApi,BrandDetailApi,BrandListApi



urlpatterns = [

    
    path('brands/',BrandList.as_view()),
    path('brands/<slug:slug>',BrandDetail.as_view()),


    path('',ProductList.as_view()),
    path('<slug:slug>',ProductDetail.as_view()),


    # api

    path('list/api',ProductListApi.as_view()),
    path('list/api/<int:pk>',ProductDetailApi.as_view()),

    path('brand/api',BrandListApi.as_view()),
    path('brand/api/<int:pk>',BrandDetailApi.as_view()),
    

    
]

