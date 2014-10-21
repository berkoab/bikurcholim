# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikurcholim', '0002_auto_20141020_2212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clients',
            old_name='current_location',
            new_name='neighborhood',
        ),
    ]
