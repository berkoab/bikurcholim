# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikurcholim', '0002_auto_20141020_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='status',
            field=models.ForeignKey(to='bikurcholim.Status'),
        ),
    ]
