# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-17 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switcher', '0029_cracknode_cs'),
    ]

    operations = [
        migrations.CreateModel(
            name='SdkNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vc', models.IntegerField(default=0)),
                ('l', models.CharField(default='', max_length=255)),
                ('ut', models.IntegerField(default=0)),
                ('et', models.IntegerField(default=0)),
            ],
        ),
    ]
