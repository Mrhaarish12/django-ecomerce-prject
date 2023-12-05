from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(Product)

class ProductImageAdmin(admin.StackedInline):
    models = ProductImage
    
admin.site.register(ProductImage)