# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-02 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20170102_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='wide_image',
            field=models.ImageField(null=True, upload_to=b'product_pics_wide'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=b'product_pics'),
        ),
    ]
