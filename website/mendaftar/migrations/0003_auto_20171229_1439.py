# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-29 07:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mendaftar', '0002_event_visitor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='about',
        ),
        migrations.RemoveField(
            model_name='event',
            name='venue',
        ),
    ]
