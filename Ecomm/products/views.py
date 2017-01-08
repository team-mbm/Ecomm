from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product
# Create your views here.
def index(request):
    items = Product.objects.all()
    print (request.__dict__)
    return render(request, 'products/index.html',{'items':items})

def all_products(request):
    items = Product.objects.all()
    return render(request, 'products/all_products.html',{'items':items})

def description(request, product_id):
    item = get_object_or_404(Product, pk=product_id)
    print (item)
    related_items =[ goods for goods in  Product.objects.filter(category=item.category) if goods.id != item.id ]
    print (related_items)
    return render(request, 'products/single-product.html', {'item':item, 'related_items':related_items})

def category_items(request, category_name):
    items = Product.objects.filter(category=category_name)
    return render(request, 'products/category.html',{'items':items})
