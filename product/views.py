from django.shortcuts import render
from .models import Category, Brand, Product

# Create your views here.
def products(request):
    products = Product.objects.order_by('-list_date').filter(category__base_category__contains="Women")[:12]

    context = {
        'products': products
    }
    # # Get Women Categories
    # women = Category.objects.filter(base_category='women')
    # # Get Men Categories
    # men = Category.objects.filter(base_category='men')
    # # Get Jewelry Categories
    # jewelry = Category.objects.filter(base_category='jewelry')
    # # Get Shoes Categories
    # shoes = Category.objects.filter(base_category='shoes')
    return render(request, 'products/categories.html', context)