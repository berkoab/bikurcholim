# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikurcholim', '0002_auto_20140921_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerOptions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('option', models.CharField(max_length=50)),
                ('choice', models.NullBooleanField()),
                ('notes', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Volunteers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('street_number', models.IntegerField(default=0)),
                ('work_place', models.CharField(max_length=100)),
                ('medical_training', models.CharField(max_length=100)),
                ('home_phone', models.CharField(max_length=50)),
                ('cell_phone', models.CharField(max_length=50)),
                ('text', models.NullBooleanField()),
                ('want_alerts', models.NullBooleanField()),
                ('neighborhood', models.ForeignKey(blank=True, to='bikurcholim.Neighborhoods', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='neighborhood',
        ),
        migrations.DeleteModel(
            name='Volunteer',
        ),
        migrations.AddField(
            model_name='volunteeroptions',
            name='volunteer',
            field=models.ForeignKey(to='bikurcholim.Volunteers'),
            preserve_default=True,
        ),
    ]
