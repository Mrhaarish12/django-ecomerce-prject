from django.shortcuts import render

# Create your views here.

def get_products(request, slug):
    try:
        return render(request, 'product/products.html')
    except Exception as e:
        print(e)