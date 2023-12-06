from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline):
    models = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productr_name']
    inlines = [ProductImageAdmin]

@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    model = ColorVariant

@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    model = SizeVariant    

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)