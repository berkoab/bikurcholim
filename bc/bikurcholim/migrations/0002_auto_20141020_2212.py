# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikurcholim', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='close_date',
            field=models.DateTimeField(null=True, verbose_name=b'close date', blank=True),
        ),
        migrations.AlterField(
            model_name='cases',
            name='date_of_service',
            field=models.DateTimeField(null=True, verbose_name=b'service date', blank=True),
        ),
        migrations.AlterField(
            model_name='cases',
            name='description',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cases',
            name='open_date',
            field=models.DateTimeField(null=True, verbose_name=b'open date', blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='donation_made',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
