# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160825_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='empresas.Empresa', verbose_name='Empresa'),
        ),
    ]