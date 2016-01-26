# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import popit.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', popit.fields.ApiInstanceURLField(help_text=b"The full URL to the root of the api - eg 'http://example.com/api", unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('popit_url', popit.fields.PopItURLField(default=b'', unique=True, null=True, blank=True)),
                ('popit_id', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200)),
                ('image', models.URLField(blank=True)),
                ('summary', models.TextField(blank=True)),
                ('api_instance', models.ForeignKey(to='popit.ApiInstance')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
