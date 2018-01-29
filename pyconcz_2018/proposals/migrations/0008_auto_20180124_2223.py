# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-24 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0007_auto_20180124_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='finaid_details',
            field=models.TextField(blank=True, help_text='Please state explicitly:\n1) why you need it,\n2) what for and\n3) how much in EUR or CZK.\nIf you require aid for more items (accommodation, travel costs etc.) please state the amount for each item.', null=True, verbose_name='Details about required financial aid'),
        ),
    ]