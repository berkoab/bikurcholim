# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikurcholim', '0003_auto_20141020_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Case Statuses',
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Status',
            new_name='ClientStatus',
        ),
        migrations.AlterModelOptions(
            name='clientstatus',
            options={'verbose_name_plural': 'Client Statuses'},
        ),
        migrations.RenameField(
            model_name='clients',
            old_name='current_location',
            new_name='neighborhood',
        ),
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
            model_name='cases',
            name='status',
            field=models.ForeignKey(to='bikurcholim.CaseStatus'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='donation_made',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='able_to_entertain_children_notes',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='assist_homebound_notes',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='assist_with_children_activities_notes',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='assist_with_children_notes',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='assist_with_housekeeping_notes',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='hospital_visitation_notes',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='learn_with_elderly_notes',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='meal_delivery_notes',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='meal_preparation_notes',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='overnight_hospital_stays_notes',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='phone_calls_notes',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='transportation_to_appointments_notes',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='visit_elderly_notes',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='wants_alerts_notes',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True),
        ),
    ]
