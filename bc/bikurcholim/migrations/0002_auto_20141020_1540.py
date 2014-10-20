# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bikurcholim', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='ClientStatus',
            new_name='Status',
        ),
        migrations.DeleteModel(
            name='CaseStatus',
        ),
        migrations.RemoveField(
            model_name='volunteeroptions',
            name='option',
        ),
        migrations.RemoveField(
            model_name='volunteeroptions',
            name='volunteers',
        ),
        migrations.DeleteModel(
            name='VolunteerOptions',
        ),
        migrations.DeleteModel(
            name='VolunteerOptionValues',
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Statuses'},
        ),
        migrations.RemoveField(
            model_name='clients',
            name='client_status',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='street',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='street_number',
        ),
        migrations.AddField(
            model_name='cases',
            name='created_at',
            field=models.DateTimeField(default=datetime.date(2014, 10, 20), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cases',
            name='service',
            field=models.ForeignKey(blank=True, to='bikurcholim.Services', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cases',
            name='updated_at',
            field=models.DateTimeField(default=datetime.date(2014, 10, 20), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clients',
            name='address',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clients',
            name='created_at',
            field=models.DateTimeField(default=datetime.date(2014, 10, 20), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clients',
            name='donation_made',
            field=models.TextField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clients',
            name='meal_coordinator',
            field=models.ForeignKey(related_name=b'meal_coordinator_set', blank=True, to='bikurcholim.Volunteers', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clients',
            name='meal_preparer',
            field=models.ForeignKey(related_name=b'meal_preparer_set', blank=True, to='bikurcholim.Volunteers', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clients',
            name='status',
            field=models.ForeignKey(blank=True, to='bikurcholim.Status', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clients',
            name='updated_at',
            field=models.DateTimeField(default=datetime.date(2014, 10, 20), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='able_to_entertain_children',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='able_to_entertain_children_notes',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='assist_homebound',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='assist_homebound_notes',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='assist_with_children',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='assist_with_children_activities',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='assist_with_children_activities_notes',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='assist_with_children_notes',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='assist_with_housekeeping',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='assist_with_housekeeping_notes',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='created_at',
            field=models.DateTimeField(default=datetime.date(2014, 10, 20), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='hospital_visitation',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='hospital_visitation_notes',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='learn_with_elderly',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='learn_with_elderly_notes',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='meal_delivery',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='meal_delivery_notes',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='meal_preparation',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='meal_preparation_notes',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='overnight_hospital_stays',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='overnight_hospital_stays_notes',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='phone_calls',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='phone_calls_notes',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='transportation_to_appointments',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='transportation_to_appointments_notes',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='updated_at',
            field=models.DateTimeField(default=datetime.date(2014, 10, 20), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='visit_elderly',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='visit_elderly_notes',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='wants_alerts',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='wants_alerts_notes',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cases',
            name='close_date',
            field=models.DateTimeField(default=None, verbose_name=b'close date'),
        ),
        migrations.AlterField(
            model_name='cases',
            name='date_of_service',
            field=models.DateTimeField(default=None, verbose_name=b'service date'),
        ),
        migrations.AlterField(
            model_name='cases',
            name='description',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cases',
            name='open_date',
            field=models.DateTimeField(default=None, verbose_name=b'open date'),
        ),
        migrations.AlterField(
            model_name='cases',
            name='volunteer',
            field=models.ForeignKey(blank=True, to='bikurcholim.Volunteers', null=True),
        ),
		migrations.AlterField(
            model_name='cases',
            name='status',
            field=models.ForeignKey(blank=True, to='bikurcholim.Status', null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='allergies',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='cell_phone',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='cholov_yisroel',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='clients',
            name='city',
            field=models.ForeignKey(blank=True, to='bikurcholim.Cities', null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='current_location',
            field=models.ForeignKey(blank=True, to='bikurcholim.Neighborhoods', null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='email_address',
            field=models.EmailField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='end_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='clients',
            name='expected_end_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='clients',
            name='food_notes',
            field=models.TextField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='food_to_home',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='clients',
            name='food_to_hospital',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='clients',
            name='home_phone',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='hospital',
            field=models.ForeignKey(blank=True, to='bikurcholim.Hospitals', null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='hospital_notes',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='hospital_room',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='medical_equipment',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='start_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='clients',
            name='text_ability',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='clients',
            name='tikvah_house',
            field=models.ForeignKey(blank=True, to='bikurcholim.TikvahHouses', null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='tikvah_room',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='transportation',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='visitor_comments',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='yoshon',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='address',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='city',
            field=models.ForeignKey(blank=True, to='bikurcholim.Cities', null=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='days_and_times_available_notes',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='email_address',
            field=models.EmailField(max_length=75, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='home_phone',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='medical_training',
            field=models.TextField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='neighborhood',
            field=models.ForeignKey(blank=True, to='bikurcholim.Neighborhoods', null=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='other_languages',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='other_specialties',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='work_place',
            field=models.TextField(max_length=100, null=True, blank=True),
        ),
    ]
