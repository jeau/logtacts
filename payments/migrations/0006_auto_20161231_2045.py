# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-31 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_stripesubscription_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stripesubscription',
            name='plan',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]