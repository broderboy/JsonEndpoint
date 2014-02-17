# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'JsonEndpoint'
        db.create_table(u'endpoint_jsonendpoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('blob', self.gf('jsonfield.fields.JSONField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
        ))
        db.send_create_signal(u'endpoint', ['JsonEndpoint'])


    def backwards(self, orm):
        # Deleting model 'JsonEndpoint'
        db.delete_table(u'endpoint_jsonendpoint')


    models = {
        u'endpoint.jsonendpoint': {
            'Meta': {'object_name': 'JsonEndpoint'},
            'blob': ('jsonfield.fields.JSONField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['endpoint']