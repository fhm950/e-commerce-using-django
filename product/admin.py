from django.contrib import admin
from .models import Category, Sub_Category, Brand, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):  
    list_display = ('category', 'added_by', 'created_at', 'is_new')
    list_display_links = ('category',)
    list_filter = ('category',)
    list_editable = ('is_new',)
    search_fields = ['category', 'added_by__username']
    list_per_page = 25


class Sub_CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'sub_category', 'starting_price', 'is_new', 'added_by')
    list_display_links = ('category', 'sub_category')
    list_filter = ('category', 'sub_category')
    list_editable = ('starting_price', 'is_new')
    search_fields = ['category__category', 'sub_category']
    list_per_page = 25

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'representative_name', 'contact_no', 'join_date')
    list_display_links = ('name',)
    list_filter = ('join_date',)
    list_editable = ('representative_name', 'contact_no')
    filter_horizontal = ('category',)
    search_fields = ['name', 'representative_name', 'category__category', 'sub_category__sub_category']
    list_per_page = 25


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'price', 'is_available', 'quantity', 'returns')
    list_display_links = ('title', 'brand')
    list_filter = ('title', 'brand', 'price', 'is_available', 'quantity')
    list_editable = ('price', 'is_available', 'quantity', 'returns')
    search_fields = ['title', 'brand__name', 'price', 'is_available', 'quantity']
    list_per_page = 25


admin.site.register(Category, CategoryAdmin)
admin.site.register(Sub_Category, Sub_CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
