# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 13:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='workplace',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Company'),
        ),
    ]
