# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-25 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switcher', '0025_auto_20170719_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='cracknode',
            name='je',
            field=models.BooleanField(default=True),
        ),
    ]
