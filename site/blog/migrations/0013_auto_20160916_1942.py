# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-16 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20160916_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='/media/placehold 900x300.png', upload_to=''),
        ),
    ]
