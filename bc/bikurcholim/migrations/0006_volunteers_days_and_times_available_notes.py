# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikurcholim', '0005_auto_20140928_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteers',
            name='days_and_times_available_notes',
            field=models.TextField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
