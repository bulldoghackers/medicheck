# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 11:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_auto_20170415_0659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='doctor',
            new_name='index',
        ),
    ]
