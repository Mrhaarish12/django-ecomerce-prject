from django.db import models

# Create your models here.
from base.models import BaseModel

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload="categories")


class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    category = models.ForiegnKey(Category, on_delete=models.CASCADE, related_name="category")
    price = models.IntegerField()
    product_description = models.TextField()


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to='products')
