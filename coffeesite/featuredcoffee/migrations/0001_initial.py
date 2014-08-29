# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Month'
        db.create_table(u'featuredcoffee_month', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('featuredcoffee', ['Month'])

        # Adding model 'Coffee'
        db.create_table(u'featuredcoffee_coffee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('highlight_month', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['featuredcoffee.Month'])),
            ('highlight_year', self.gf('django.db.models.fields.IntegerField')(default=2015)),
            ('origin', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('sort_number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('featuredcoffee', ['Coffee'])


    def backwards(self, orm):
        # Deleting model 'Month'
        db.delete_table(u'featuredcoffee_month')

        # Deleting model 'Coffee'
        db.delete_table(u'featuredcoffee_coffee')


    models = {
        'featuredcoffee.coffee': {
            'Meta': {'object_name': 'Coffee'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'highlight_month': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['featuredcoffee.Month']"}),
            'highlight_year': ('django.db.models.fields.IntegerField', [], {'default': '2015'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'sort_number': ('django.db.models.fields.IntegerField', [], {})
        },
        'featuredcoffee.month': {
            'Meta': {'object_name': 'Month'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['featuredcoffee']