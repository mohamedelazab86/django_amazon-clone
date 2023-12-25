from django.urls import path
from .views import ProductList,ProductDetail,BrandDetail,BrandList
urlpatterns = [

    
    path('brands/',BrandList.as_view()),
    path('brands/<slug:slug>',BrandDetail.as_view()),


    path('',ProductList.as_view()),
    path('<slug:slug>',ProductDetail.as_view()),

    
]

