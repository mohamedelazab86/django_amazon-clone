from rest_framework import serializers
from .models import Product,Brand,Review,ProductImage



class Imageserializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fields=['image']
class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['user','rate','publish_date']

class ProductListSerializer(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    class Meta:
        model=Product
        fields='__all__'

class ProductDetailserializer(serializers.ModelSerializer):
    images=Imageserializer(source='proimage_product',many=True)
    reviews=ReviewsSerializer(source='review_product',many=True)

    review_count=serializers.SerializerMethodField()
    rate=serializers.SerializerMethodField()

    brand=serializers.StringRelatedField()
    
    class Meta:
        model=Product
        fields='__all__'
    def get_review_count(self,object):
        reviews=object.review_product.all().count()
        return reviews
    
    def get_rate(self,object):
        total=0
        reviews=object.review_product.all()
        if len(reviews)>0:
            for review in reviews :
                total +=review.rate
                avg=total/len(reviews)

        else:
            avg=0
        return avg
  

    
        

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'

class BrandDetailserializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'
        