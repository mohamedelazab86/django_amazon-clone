from django.shortcuts import render
from .models import Product,Brand,Review,ProductImage
from django.views.generic import ListView,DetailView

# Create your views here.

# create crud opertions
class ProductList(ListView):
    model=Product
    paginate_by=50

class ProductDetail(DetailView):
    model=Product
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] =Review.objects.filter(product=self.get_object()) 
        context["images"] =ProductImage.objects.filter(product=self.get_object())
        context["products"] =Product.objects.filter(brand=self.get_object().brand)
        return context
    

class BrandList(ListView):
    model=Brand
    paginate_by=30

class BrandDetail(DetailView):
    model=Brand
