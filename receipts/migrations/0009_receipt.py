# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 05:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20171110_0333'),
        ('receipts', '0008_auto_20171113_0504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('payer', models.CharField(max_length=30)),
                ('payee', models.CharField(max_length=30)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('address', models.CharField(max_length=80)),
                ('notes', models.CharField(blank=True, max_length=80)),
                ('receipt_id', models.TextField(default='<django.db.models.fields.DateField>-<built-in function id>', primary_key=True, serialize=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Staff')),
                ('items', models.ManyToManyField(to='receipts.Item')),
            ],
        ),
    ]
