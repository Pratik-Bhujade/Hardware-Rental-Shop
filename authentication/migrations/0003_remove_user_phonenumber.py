# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-25 07:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20190325_0743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phoneNumber',
        ),
    ]
