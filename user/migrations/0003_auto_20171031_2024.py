# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 20:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_visitors'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Visitors',
            new_name='Visitor',
        ),
    ]
