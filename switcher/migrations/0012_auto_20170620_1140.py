# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-20 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('switcher', '0011_auto_20170620_0546'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrackContext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=255)),
                ('pkg_name', models.CharField(max_length=255)),
                ('version_name', models.CharField(max_length=255)),
                ('version_code', models.IntegerField(default=0)),
                ('label', models.CharField(max_length=255)),
                ('signatures', models.TextField()),
                ('extra', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CrackNode',
            fields=[
                ('pkg_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CrackPlacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField(default=0)),
                ('extra', models.TextField(default='')),
                ('crack_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crack_node', to='switcher.CrackNode')),
            ],
        ),
        migrations.DeleteModel(
            name='AdContext',
        ),
        migrations.AddField(
            model_name='crackcontext',
            name='crack_node',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='switcher.CrackNode'),
        ),
    ]