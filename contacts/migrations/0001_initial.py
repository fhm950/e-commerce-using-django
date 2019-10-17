# Generated by Django 2.2.5 on 2019-09-10 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=200)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
