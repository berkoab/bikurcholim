# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikurcholim', '0002_auto_20141020_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='expected_end_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
