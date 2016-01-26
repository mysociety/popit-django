# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ApiInstance'
        db.create_table(u'popit_apiinstance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('popit.fields.ApiInstanceURLField')(unique=True, max_length=200)),
        ))
        db.send_create_signal(u'popit', ['ApiInstance'])


    def backwards(self, orm):
        # Deleting model 'ApiInstance'
        db.delete_table(u'popit_apiinstance')


    models = {
        u'popit.apiinstance': {
            'Meta': {'object_name': 'ApiInstance'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('popit.fields.ApiInstanceURLField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['popit']