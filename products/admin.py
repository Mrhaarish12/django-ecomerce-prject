from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(Product)

class ProductImageAdmin(admin.StackedInline):
    models = ProductImage

class Product(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    
admin.site.register(ProductImage)