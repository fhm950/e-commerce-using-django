# Generated by Django 2.2.5 on 2019-10-09 10:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('logo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('representative_name', models.CharField(max_length=100)),
                ('contact_no', phone_field.models.PhoneField(max_length=31, unique=True)),
                ('join_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_available', models.BooleanField(default=True)),
                ('quantity', models.IntegerField()),
                ('information', models.CharField(max_length=500)),
                ('length', models.CharField(max_length=200)),
                ('fibres', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=200)),
                ('care_details', models.CharField(max_length=200)),
                ('returns', models.IntegerField(default=7)),
                ('cash_on_delivery', models.BooleanField(default=True)),
                ('shipping_info', models.CharField(max_length=150)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_category', models.CharField(max_length=200)),
                ('sub_category', models.CharField(max_length=200)),
                ('is_new', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='category',
            field=models.ManyToManyField(to='product.Category'),
        ),
    ]