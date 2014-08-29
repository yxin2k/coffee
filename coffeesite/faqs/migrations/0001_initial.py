# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FaqsCategory'
        db.create_table(u'faqs_faqscategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('faqs', ['FaqsCategory'])

        # Adding model 'Faqs'
        db.create_table(u'faqs_faqs', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['faqs.FaqsCategory'])),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('faqs', ['Faqs'])


    def backwards(self, orm):
        # Deleting model 'FaqsCategory'
        db.delete_table(u'faqs_faqscategory')

        # Deleting model 'Faqs'
        db.delete_table(u'faqs_faqs')


    models = {
        'faqs.faqs': {
            'Meta': {'object_name': 'Faqs'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['faqs.FaqsCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        },
        'faqs.faqscategory': {
            'Meta': {'object_name': 'FaqsCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['faqs']