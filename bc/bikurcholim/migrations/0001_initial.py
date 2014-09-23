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
                ('open_date', models.DateTimeField(verbose_name=b'open date')),
                ('date_of_service', models.DateTimeField(verbose_name=b'service date')),
                ('close_date', models.DateTimeField(verbose_name=b'close date')),
                ('description', models.CharField(max_length=200)),
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
                ('start_date', models.DateTimeField(verbose_name=b'start date')),
                ('expected_end_date', models.DateTimeField(verbose_name=b'expected end date')),
                ('end_date', models.DateTimeField(verbose_name=b'end date')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('street_number', models.IntegerField()),
                ('street', models.CharField(max_length=50)),
                ('home_phone', models.CharField(max_length=50)),
                ('cell_phone', models.CharField(max_length=50)),
                ('text_ability', models.NullBooleanField()),
                ('email_address', models.CharField(max_length=50, null=True)),
                ('hospital_room', models.CharField(max_length=50)),
                ('hospital_notes', models.CharField(max_length=200)),
                ('tikvah_room', models.CharField(max_length=50)),
                ('food_to_hospital', models.NullBooleanField()),
                ('food_notes', models.CharField(max_length=300)),
                ('food_to_home', models.NullBooleanField()),
                ('allergies', models.CharField(max_length=200)),
                ('yoshon', models.NullBooleanField()),
                ('cholov_yisroel', models.NullBooleanField()),
                ('transportation', models.CharField(max_length=200)),
                ('visitor_comments', models.CharField(max_length=500)),
                ('medical_equipment', models.CharField(max_length=200)),
                ('city', models.ForeignKey(to='bikurcholim.Cities', null=True)),
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
                ('address', models.CharField(max_length=200)),
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
            name='TikvahHouses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
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
            name='VolunteerOptions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.NullBooleanField()),
                ('notes', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Volunteer Options',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VolunteerOptionValues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('option', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Volunteer Option Values',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Volunteers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('street_number', models.IntegerField()),
                ('street', models.CharField(max_length=50, null=True)),
                ('work_place', models.CharField(max_length=100)),
                ('medical_training', models.CharField(max_length=100)),
                ('home_phone', models.CharField(max_length=50)),
                ('cell_phone', models.CharField(max_length=50)),
                ('email_address', models.CharField(max_length=50, null=True)),
                ('days_times_available', models.CharField(max_length=200, null=True)),
                ('other_languages', models.CharField(max_length=200, null=True)),
                ('other_specialties', models.CharField(max_length=200, null=True)),
                ('neighborhood', models.ForeignKey(to='bikurcholim.Neighborhoods', null=True)),
                ('vehicle', models.ForeignKey(blank=True, to='bikurcholim.Vehicles', null=True)),
            ],
            options={
                'verbose_name_plural': 'Volunteers',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='volunteeroptions',
            name='option',
            field=models.ForeignKey(to='bikurcholim.VolunteerOptionValues'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteeroptions',
            name='volunteers',
            field=models.ForeignKey(to='bikurcholim.Volunteers'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clients',
            name='client_status',
            field=models.ForeignKey(to='bikurcholim.ClientStatus', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clients',
            name='current_location',
            field=models.ForeignKey(to='bikurcholim.Neighborhoods', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clients',
            name='hospital',
            field=models.ForeignKey(to='bikurcholim.Hospitals', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clients',
            name='tikvah_house',
            field=models.ForeignKey(to='bikurcholim.TikvahHouses', null=True),
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
            name='status',
            field=models.ForeignKey(to='bikurcholim.CaseStatus'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cases',
            name='volunteer',
            field=models.ForeignKey(to='bikurcholim.Volunteers', null=True),
            preserve_default=True,
        ),
    ]
