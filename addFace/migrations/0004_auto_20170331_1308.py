# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 13:08
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addFace', '0003_auto_20170331_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='encode',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), size=None),
        ),
    ]