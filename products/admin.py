from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline):
    models = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    model = ColorVariant

class SizeVariantAdmin(admin.ModelAdmin):
    model = SizeVariant    

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)