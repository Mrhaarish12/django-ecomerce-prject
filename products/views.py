from django.shortcuts import render

# Create your views here.

def get_producgts(request, slug):
    return render(request, 'product/products.html')