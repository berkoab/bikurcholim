# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikurcholim', '0004_auto_20140924_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteerdaysavailable',
            name='volunteers',
        ),
        migrations.DeleteModel(
            name='VolunteerDaysAvailable',
        ),
        migrations.AddField(
            model_name='volunteers',
            name='friday',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='monday',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='shabbos',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='sunday',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='thursday',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='tuesday',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='wednesday',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
    ]
