# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('company', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='/media/')),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
