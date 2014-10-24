# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('open_date', models.DateField(null=True, verbose_name=b'open date', blank=True)),
                ('date_of_service', models.DateTimeField(null=True, verbose_name=b'date and time of service', blank=True)),
                ('close_date', models.DateField(null=True, verbose_name=b'close date', blank=True)),
                ('description', models.TextField(max_length=200, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Cases',
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('home_phone', models.CharField(max_length=50, null=True, blank=True)),
                ('cell_phone', models.CharField(max_length=50, null=True, blank=True)),
                ('email_address', models.EmailField(max_length=50, null=True, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('expected_end_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('hospital_room', models.CharField(max_length=50, null=True, blank=True)),
                ('hospital_notes', models.TextField(max_length=200, null=True, blank=True)),
                ('tikvah_room', models.CharField(max_length=50, null=True, blank=True)),
                ('food_notes', models.TextField(max_length=300, null=True, blank=True)),
                ('allergies', models.TextField(max_length=200, null=True, blank=True)),
                ('transportation', models.TextField(max_length=200, null=True, blank=True)),
                ('visitor_comments', models.TextField(max_length=500, null=True, blank=True)),
                ('medical_equipment', models.TextField(max_length=200, null=True, blank=True)),
                ('donation_made', models.CharField(max_length=50, null=True, blank=True)),
                ('text_ability', models.BooleanField(default=None)),
                ('yoshon', models.BooleanField(default=None)),
                ('cholov_yisroel', models.BooleanField(default=None)),
                ('food_to_hospital', models.BooleanField(default=None)),
                ('food_to_home', models.BooleanField(default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(blank=True, to='bikurcholim.Cities', null=True)),
            ],
            options={
                'verbose_name_plural': 'Clients',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Client Statuses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hospitals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Hospitals',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Neighborhoods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('neighborhood', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Neighborhoods',
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='TikvahHouses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Tikvah Houses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vehicle', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Vehicles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Volunteers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('work_place', models.TextField(max_length=100, null=True, blank=True)),
                ('medical_training', models.TextField(max_length=100, null=True, blank=True)),
                ('home_phone', models.CharField(max_length=50, null=True, blank=True)),
                ('cell_phone', models.CharField(max_length=50, null=True, blank=True)),
                ('email_address', models.EmailField(max_length=75, null=True, blank=True)),
                ('other_languages', models.TextField(max_length=200, null=True, blank=True)),
                ('other_specialties', models.TextField(max_length=200, null=True, blank=True)),
                ('days_and_times_available_notes', models.TextField(max_length=200, null=True, verbose_name=b'Notes on Availability', blank=True)),
                ('start_time_available', models.TimeField(null=True, verbose_name=b'Available From', blank=True)),
                ('end_time_availalable', models.TimeField(null=True, verbose_name=b'Available To', blank=True)),
                ('sunday', models.BooleanField(default=None)),
                ('monday', models.BooleanField(default=None)),
                ('tuesday', models.BooleanField(default=None)),
                ('wednesday', models.BooleanField(default=None)),
                ('thursday', models.BooleanField(default=None)),
                ('friday', models.BooleanField(default=None)),
                ('shabbos', models.BooleanField(default=None)),
                ('wants_alerts', models.BooleanField(default=None)),
                ('wants_alerts_notes', models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True)),
                ('meal_preparation', models.BooleanField(default=None)),
                ('meal_preparation_notes', models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True)),
                ('meal_delivery', models.BooleanField(default=None)),
                ('meal_delivery_notes', models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True)),
                ('hospital_visitation', models.BooleanField(default=None)),
                ('hospital_visitation_notes', models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True)),
                ('transportation_to_appointments', models.BooleanField(default=None)),
                ('transportation_to_appointments_notes', models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True)),
                ('overnight_hospital_stays', models.BooleanField(default=None)),
                ('overnight_hospital_stays_notes', models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True)),
                ('assist_homebound', models.BooleanField(default=None)),
                ('assist_homebound_notes', models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True)),
                ('assist_with_children', models.BooleanField(default=None)),
                ('assist_with_children_notes', models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True)),
                ('assist_with_children_activities', models.BooleanField(default=None)),
                ('assist_with_children_activities_notes', models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True)),
                ('able_to_entertain_children', models.BooleanField(default=None)),
                ('able_to_entertain_children_notes', models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True)),
                ('visit_elderly', models.BooleanField(default=None)),
                ('visit_elderly_notes', models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True)),
                ('assist_with_housekeeping', models.BooleanField(default=None)),
                ('assist_with_housekeeping_notes', models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True)),
                ('phone_calls', models.BooleanField(default=None)),
                ('phone_calls_notes', models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True)),
                ('learn_with_elderly', models.BooleanField(default=None)),
                ('learn_with_elderly_notes', models.CharField(max_length=100, null=True, verbose_name=b'Notes', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(blank=True, to='bikurcholim.Cities', null=True)),
                ('neighborhood', models.ForeignKey(blank=True, to='bikurcholim.Neighborhoods', null=True)),
                ('vehicle', models.ForeignKey(blank=True, to='bikurcholim.Vehicles', null=True)),
            ],
            options={
                'verbose_name_plural': 'Volunteers',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='clients',
            name='hospital',
            field=models.ForeignKey(blank=True, to='bikurcholim.Hospitals', null=True),
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
            name='neighborhood',
            field=models.ForeignKey(blank=True, to='bikurcholim.Neighborhoods', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clients',
            name='status',
            field=models.ForeignKey(blank=True, to='bikurcholim.ClientStatus', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clients',
            name='tikvah_house',
            field=models.ForeignKey(blank=True, to='bikurcholim.TikvahHouses', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cases',
            name='client',
            field=models.ForeignKey(to='bikurcholim.Clients'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cases',
            name='service',
            field=models.ForeignKey(blank=True, to='bikurcholim.Services', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cases',
            name='status',
            field=models.ForeignKey(to='bikurcholim.CaseStatus'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cases',
            name='volunteer',
            field=models.ForeignKey(blank=True, to='bikurcholim.Volunteers', null=True),
            preserve_default=True,
        ),
    ]
