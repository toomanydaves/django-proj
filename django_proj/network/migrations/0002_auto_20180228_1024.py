# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-28 10:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='peep',
            old_name='picture',
            new_name='profile_picture',
        ),
    ]
