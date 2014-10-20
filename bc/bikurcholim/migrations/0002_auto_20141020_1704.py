# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikurcholim', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteers',
            name='cell_phone',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='end_time_availalable',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='start_time_available',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
