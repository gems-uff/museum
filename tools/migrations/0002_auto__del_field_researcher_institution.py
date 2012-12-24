# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Researcher.institution'
        db.delete_column('tools_researcher', 'institution_id')

        # Adding M2M table for field affiliation on 'Researcher'
        db.create_table('tools_researcher_affiliation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('researcher', models.ForeignKey(orm['tools.researcher'], null=False)),
            ('institution', models.ForeignKey(orm['tools.institution'], null=False))
        ))
        db.create_unique('tools_researcher_affiliation', ['researcher_id', 'institution_id'])


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Researcher.institution'
        raise RuntimeError("Cannot reverse this migration. 'Researcher.institution' and its values cannot be restored.")
        # Removing M2M table for field affiliation on 'Researcher'
        db.delete_table('tools_researcher_affiliation')


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
            'affiliation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tools.Institution']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['tools']