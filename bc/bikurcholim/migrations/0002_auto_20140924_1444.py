# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikurcholim', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerDaysAvailable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sunday', models.BooleanField(default=None)),
                ('monday', models.NullBooleanField()),
                ('tuesday', models.NullBooleanField()),
                ('wednesday', models.NullBooleanField()),
                ('thursday', models.NullBooleanField()),
                ('friday', models.NullBooleanField()),
                ('shabbos', models.NullBooleanField()),
                ('volunteers', models.ForeignKey(to='bikurcholim.Volunteers')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='volunteers',
            name='days_times_available',
        ),
        migrations.RemoveField(
            model_name='volunteers',
            name='street',
        ),
        migrations.RemoveField(
            model_name='volunteers',
            name='street_number',
        ),
        migrations.AddField(
            model_name='volunteers',
            name='address',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='city',
            field=models.ForeignKey(to='bikurcholim.Cities', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='end_time_availalable',
            field=models.TimeField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='start_time_available',
            field=models.TimeField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='clients',
            name='allergies',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='clients',
            name='email_address',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='end_date',
            field=models.DateField(verbose_name=b'end date'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='expected_end_date',
            field=models.DateField(verbose_name=b'expected end date'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='food_notes',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='clients',
            name='hospital_notes',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='clients',
            name='medical_equipment',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='clients',
            name='start_date',
            field=models.DateField(verbose_name=b'start date'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='transportation',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='clients',
            name='visitor_comments',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='email_address',
            field=models.EmailField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='medical_training',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='other_languages',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='other_specialties',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='work_place',
            field=models.TextField(max_length=100),
        ),
    ]
