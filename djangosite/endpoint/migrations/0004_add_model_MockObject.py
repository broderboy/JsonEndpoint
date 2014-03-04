# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MockObject'
        db.create_table(u'endpoint_mockobject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('mock_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['endpoint.MockObjectClass'])),
            ('blob', self.gf('jsonfield.fields.JSONField')()),
        ))
        db.send_create_signal(u'endpoint', ['MockObject'])


    def backwards(self, orm):
        # Deleting model 'MockObject'
        db.delete_table(u'endpoint_mockobject')


    models = {
        u'endpoint.authendpoint': {
            'Meta': {'object_name': 'AuthEndpoint'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'endpoint.jsonendpoint': {
            'Meta': {'ordering': "['name']", 'object_name': 'JsonEndpoint'},
            'blob': ('jsonfield.fields.JSONField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'endpoint.mockobject': {
            'Meta': {'object_name': 'MockObject'},
            'blob': ('jsonfield.fields.JSONField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mock_class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['endpoint.MockObjectClass']"}),
            'object_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'endpoint.mockobjectclass': {
            'Meta': {'object_name': 'MockObjectClass'},
            'class_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['endpoint']