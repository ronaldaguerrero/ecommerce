# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-01 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(default=None, max_length=2),
        ),
    ]
