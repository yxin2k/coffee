# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'memberships_userprofile', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('isSubscribed', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('isEmailOptIn', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('memberships', ['UserProfile'])

        # Adding model 'Province'
        db.create_table(u'memberships_province', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('memberships', ['Province'])

        # Adding model 'Country'
        db.create_table(u'memberships_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('memberships', ['Country'])

        # Adding model 'ShippingAddress'
        db.create_table(u'memberships_shippingaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('provinceId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['memberships.Province'])),
            ('postalCode', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('countryId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['memberships.Country'])),
        ))
        db.send_create_signal('memberships', ['ShippingAddress'])

        # Adding model 'BillingAddress'
        db.create_table(u'memberships_billingaddress', (
            ('userId', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('provinceId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['memberships.Province'])),
            ('postalCode', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('countryId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['memberships.Country'])),
        ))
        db.send_create_signal('memberships', ['BillingAddress'])

        # Adding model 'GrindType'
        db.create_table(u'memberships_grindtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('isActive', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('memberships', ['GrindType'])

        # Adding model 'SubscriptionType'
        db.create_table(u'memberships_subscriptiontype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('memberships', ['SubscriptionType'])

        # Adding model 'SubscriptionPreferences'
        db.create_table(u'memberships_subscriptionpreferences', (
            ('userId', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('grindType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['memberships.GrindType'])),
            ('isSubPaused', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('subPauseDate', self.gf('django.db.models.fields.DateField')()),
            ('subStartDate', self.gf('django.db.models.fields.DateField')()),
            ('subEndDate', self.gf('django.db.models.fields.DateField')()),
            ('subType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['memberships.SubscriptionType'])),
            ('shippingAddress', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['memberships.ShippingAddress'])),
            ('billingAddress', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['memberships.BillingAddress'], unique=True)),
        ))
        db.send_create_signal('memberships', ['SubscriptionPreferences'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'memberships_userprofile')

        # Deleting model 'Province'
        db.delete_table(u'memberships_province')

        # Deleting model 'Country'
        db.delete_table(u'memberships_country')

        # Deleting model 'ShippingAddress'
        db.delete_table(u'memberships_shippingaddress')

        # Deleting model 'BillingAddress'
        db.delete_table(u'memberships_billingaddress')

        # Deleting model 'GrindType'
        db.delete_table(u'memberships_grindtype')

        # Deleting model 'SubscriptionType'
        db.delete_table(u'memberships_subscriptiontype')

        # Deleting model 'SubscriptionPreferences'
        db.delete_table(u'memberships_subscriptionpreferences')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'memberships.billingaddress': {
            'Meta': {'object_name': 'BillingAddress'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'countryId': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['memberships.Country']"}),
            'postalCode': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'provinceId': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['memberships.Province']"}),
            'userId': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'memberships.country': {
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'memberships.grindtype': {
            'Meta': {'object_name': 'GrindType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isActive': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'memberships.province': {
            'Meta': {'object_name': 'Province'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'memberships.shippingaddress': {
            'Meta': {'object_name': 'ShippingAddress'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'countryId': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['memberships.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postalCode': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'provinceId': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['memberships.Province']"}),
            'userId': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'memberships.subscriptionpreferences': {
            'Meta': {'object_name': 'SubscriptionPreferences'},
            'billingAddress': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['memberships.BillingAddress']", 'unique': 'True'}),
            'grindType': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['memberships.GrindType']"}),
            'isSubPaused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shippingAddress': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['memberships.ShippingAddress']"}),
            'subEndDate': ('django.db.models.fields.DateField', [], {}),
            'subPauseDate': ('django.db.models.fields.DateField', [], {}),
            'subStartDate': ('django.db.models.fields.DateField', [], {}),
            'subType': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['memberships.SubscriptionType']"}),
            'userId': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'memberships.subscriptiontype': {
            'Meta': {'object_name': 'SubscriptionType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'memberships.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'isEmailOptIn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isSubscribed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['memberships']