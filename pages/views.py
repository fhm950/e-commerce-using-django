from django.shortcuts import render
from product.models import Category, Product


def index(request):
    # Get Hero Section
    hero_sections = Category.objects.order_by('-updated_at').filter(is_new=True)[:2]
    # Get Latest Products
    latest_products = Product.objects.order_by('-list_date').filter(is_available=True)[:8]
    # Get Banner Section
    banner_sections = Category.objects.order_by('-updated_at').filter(is_new=True)[0]
    # Get Catagories on Navbar
    base_categories = Category.objects.order_by('-updated_at').filter(is_new=True)[:]
    # Get Sub-Category on Navbar
    sub_categories = Category.objects.order_by('-updated_at').filter(is_new=True)[:]

    context = {
        'latest_products': latest_products,
        'hero_sections': hero_sections,
        'banner_sections': banner_sections,
        'base_categories': base_categories,
        'sub_categories': sub_categories
    }
    return render(request, 'pages/index.html', context)



