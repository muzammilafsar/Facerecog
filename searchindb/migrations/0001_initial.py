# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('date', models.DateTimeField(auto_created=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
