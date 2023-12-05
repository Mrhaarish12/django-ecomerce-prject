from django.urls import path
from products.views import get_product

urlspatterns = [
    path('<slug>/', get_product , name="get_product")
]