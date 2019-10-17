from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from phone_field import PhoneField

# Create your models here.

# Category Model
class Category(models.Model):
    category = models.CharField(max_length=200, null=False)
    is_new = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.category


class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    sub_category = models.CharField(max_length=200, null=False)
    hero_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, null=True)
    banner_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, null=True)
    description = models.CharField(max_length=200, blank=False, null=True)
    starting_price = models.IntegerField(null=True)
    is_new = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.sub_category

# Brand Model
class Brand(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)
    logo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    representative_name = models.CharField(max_length=100, null=False)
    contact_no = PhoneField(null=False, unique=True)
    join_date = models.DateTimeField(default=datetime.now, blank=True)
    category = models.ManyToManyField(Category)
    sub_category = models.ManyToManyField(Sub_Category)

    def __str__(self):
        return self.name


# Product Model
class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.DO_NOTHING, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    ratings = GenericRelation(Rating, related_query_name='stars')
    quantity = models.IntegerField()
    information = models.CharField(max_length=500, null=False)
    length = models.CharField(max_length=200, null=False)
    fibres = models.CharField(max_length=200, null=False)
    size = models.CharField(max_length=200, null=False)
    care_details = models.CharField(max_length=200, null=False)
    returns = models.IntegerField(default=7)
    cash_on_delivery = models.BooleanField(default=True)
    shipping_info = models.CharField(max_length=150)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    list_date = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.title