# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-02 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20171102_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='creation_time',
            field=models.CharField(default='2017-11-02 13:45:16', max_length=250),
        ),
    ]
