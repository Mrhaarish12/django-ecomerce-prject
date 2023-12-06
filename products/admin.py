from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline):
    models = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

class ColorVariantAdmin(admin.ModelAdmin):
    model = ColorVariant

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)