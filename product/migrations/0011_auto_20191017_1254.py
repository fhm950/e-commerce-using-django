# Generated by Django 2.2.5 on 2019-10-17 06:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0010_auto_20191011_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='base_category',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='category',
            name='banner_photo',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='hero_photo',
        ),
        migrations.RemoveField(
            model_name='category',
            name='starting_price',
        ),
        migrations.RemoveField(
            model_name='category',
            name='sub_category',
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(max_length=200)),
                ('hero_photo', models.ImageField(null=True, upload_to='photos/%Y/%m/%d')),
                ('banner_photo', models.ImageField(null=True, upload_to='photos/%Y/%m/%d')),
                ('description', models.CharField(max_length=200, null=True)),
                ('starting_price', models.IntegerField(null=True)),
                ('is_new', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.Category')),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='sub_category',
            field=models.ManyToManyField(to='product.Sub_Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='product.Sub_Category'),
        ),
    ]