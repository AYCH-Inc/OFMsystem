# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_remove_information_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]