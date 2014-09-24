# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikurcholim', '0002_auto_20140924_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerdaysavailable',
            name='friday',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='volunteerdaysavailable',
            name='monday',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='volunteerdaysavailable',
            name='shabbos',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='volunteerdaysavailable',
            name='thursday',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='volunteerdaysavailable',
            name='tuesday',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='volunteerdaysavailable',
            name='wednesday',
            field=models.BooleanField(default=None),
        ),
    ]
