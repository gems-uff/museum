# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Edition'
        db.create_table('tools_edition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('tools', ['Edition'])

        # Adding model 'Institution'
        db.create_table('tools_institution', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('tools', ['Institution'])

        # Adding model 'Researcher'
        db.create_table('tools_researcher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tools.Institution'])),
        ))
        db.send_create_signal('tools', ['Researcher'])


    def backwards(self, orm):
        # Deleting model 'Edition'
        db.delete_table('tools_edition')

        # Deleting model 'Institution'
        db.delete_table('tools_institution')

        # Deleting model 'Researcher'
        db.delete_table('tools_researcher')


    models = {
        'tools.edition': {
            'Meta': {'object_name': 'Edition'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'tools.institution': {
            'Meta': {'object_name': 'Institution'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tools.researcher': {
            'Meta': {'object_name': 'Researcher'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tools.Institution']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['tools']