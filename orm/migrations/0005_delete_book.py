# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 05:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0004_auto_20171028_1511'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
