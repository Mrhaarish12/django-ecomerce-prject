from django.shortcuts import render
from products.models import Product
# Create your views here.

def get_products(request, slug):
    try:
        product = Product.objects.get(slug=slug)

        if request.GET.get('size'):
            size = request.GET.get('size')
            price = product.get_product_price_by_size()
            print(size)
        return render(request, 'product/products.html', context={'product': product})
    except Exception as e:
        print(e)