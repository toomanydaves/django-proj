# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-22 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_project_claim'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='internal_rating',
            field=models.PositiveSmallIntegerField(default=50),
        ),
    ]