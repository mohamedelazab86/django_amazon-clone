from django.contrib import admin
from .models import Product,Brand,ProductImage,Review
from django_summernote.admin import SummernoteModelAdmin



# Register your models here.

class ProductImageadmin(admin.TabularInline):
    model=ProductImage

# customize for product admin
class ProductAdmin(SummernoteModelAdmin):
    list_display=['name','flag','price']
    list_filter=['flag','brand']
    search_fields=['name']
    summernote_fields = ('subtitle','descriptions')
    inlines=[ProductImageadmin]


admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
#admin.site.register(ProductImage)
admin.site.register(Review)


