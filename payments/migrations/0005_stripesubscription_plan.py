# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-29 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_auto_20161018_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripesubscription',
            name='plan',
            field=models.CharField(blank=True, choices=[('basic_monthly', 'Basic Monthly Subscription'), ('team_monthly', 'Team Monthly Subscription'), ('basic_yearly', 'Basic Yearly Subscription'), ('family_yearly', 'Family Yearly Subscription'), ('team_yearly', 'Team Yearly Subscription'), ('family_monthly', 'Family Monthly Subscription')], max_length=255, null=True),
        ),
    ]