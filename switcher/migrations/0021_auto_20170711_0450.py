# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-11 04:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('switcher', '0020_auto_20170707_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crackcontext',
            name='crack_node',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='c', to='switcher.CrackNode'),
        ),
        migrations.AlterField(
            model_name='placement',
            name='extra',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
