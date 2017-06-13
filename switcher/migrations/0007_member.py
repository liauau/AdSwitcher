# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switcher', '0006_auto_20170606_0757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('pkg_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('image_url', models.CharField(max_length=255)),
                ('icon_url', models.CharField(max_length=255)),
                ('app_name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('action', models.CharField(max_length=255)),
            ],
        ),
    ]
