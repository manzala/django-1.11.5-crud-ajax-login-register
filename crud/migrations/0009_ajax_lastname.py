# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-04 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0008_ajax_firstname'),
    ]

    operations = [
        migrations.AddField(
            model_name='ajax',
            name='lastname',
            field=models.CharField(default='Gowthaman', max_length=40),
            preserve_default=False,
        ),
    ]
