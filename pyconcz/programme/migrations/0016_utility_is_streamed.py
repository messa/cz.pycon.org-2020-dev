# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-02-15 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0015_auto_20190605_0634'),
    ]

    operations = [
        migrations.AddField(
            model_name='utility',
            name='is_streamed',
            field=models.BooleanField(default=False, verbose_name='Is streamed to other rooms?'),
        ),
    ]
