# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 11:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veterinarias', '0003_auto_20171108_0528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veterinario',
            name='fecha_consulta',
        ),
    ]
