# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field chair on 'Edition'
        db.create_table('tools_edition_chair', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('edition', models.ForeignKey(orm['tools.edition'], null=False)),
            ('researcher', models.ForeignKey(orm['tools.researcher'], null=False))
        ))
        db.create_unique('tools_edition_chair', ['edition_id', 'researcher_id'])


    def backwards(self, orm):
        # Removing M2M table for field chair on 'Edition'
        db.delete_table('tools_edition_chair')


    models = {
        'tools.edition': {
            'Meta': {'object_name': 'Edition'},
            'chair': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tools.Researcher']", 'symmetrical': 'False'}),
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
            'affiliation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tools.Institution']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['tools']