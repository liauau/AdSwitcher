# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-20 05:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('switcher', '0010_fbcontext'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FbContext',
            new_name='AdContext',
        ),
    ]
