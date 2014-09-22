# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikurcholim', '0003_auto_20140921_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteers',
            name='text',
        ),
        migrations.RemoveField(
            model_name='volunteers',
            name='want_alerts',
        ),
    ]
