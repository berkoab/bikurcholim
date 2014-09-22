# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikurcholim', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhoods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('neighborhood', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='neighborhood',
            field=models.ForeignKey(blank=True, to='bikurcholim.Neighborhoods', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='street_number',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
