# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-16 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='/post_images', upload_to=''),
        ),
    ]
