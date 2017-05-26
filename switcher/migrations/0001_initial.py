# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 06:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppNode',
            fields=[
                ('pkg_name', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='switcher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=255)),
                ('pkg_name', models.CharField(max_length=255)),
                ('version_name', models.CharField(max_length=255)),
                ('version_code', models.IntegerField()),
                ('label', models.CharField(max_length=255)),
                ('signatures', models.CharField(max_length=255)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='context', to='switcher.AppNode')),
            ],
        ),
        migrations.CreateModel(
            name='Mix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_platform', models.CharField(max_length=255)),
                ('app', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='switcher.AppNode')),
            ],
        ),
        migrations.CreateModel(
            name='PlacementMappings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=255)),
                ('placement', models.CharField(max_length=255)),
                ('mix', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='placement_mappings', to='switcher.Mix')),
            ],
        ),
    ]