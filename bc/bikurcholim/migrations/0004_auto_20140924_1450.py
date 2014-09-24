# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikurcholim', '0003_auto_20140924_1447'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='volunteerdaysavailable',
            options={'verbose_name_plural': 'Days Available'},
        ),
        migrations.RemoveField(
            model_name='volunteeroptions',
            name='choice',
        ),
        migrations.AddField(
            model_name='volunteeroptions',
            name='has_option',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
    ]
