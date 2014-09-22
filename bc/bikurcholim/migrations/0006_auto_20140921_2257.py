# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikurcholim', '0005_auto_20140921_2137'),
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
            },
            bases=(models.Model,),
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
        migrations.AddField(
            model_name='volunteers',
            name='email_address',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='street',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='neighborhood',
            field=models.ForeignKey(to='bikurcholim.Neighborhoods', null=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='street_number',
            field=models.IntegerField(),
        ),
    ]
