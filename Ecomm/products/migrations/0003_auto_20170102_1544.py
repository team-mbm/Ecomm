# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-02 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20161229_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=b'/'),
        ),
    ]
