from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register()

class ProductImageAdmin(admin.StackedInline):
    models = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price']
    inlines = [ProductImageAdmin]

@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['color_name', 'price']
    model = ColorVariant

@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size', 'price']
    model = SizeVariant    

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)