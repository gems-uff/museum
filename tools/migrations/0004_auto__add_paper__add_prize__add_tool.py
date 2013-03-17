# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Paper'
        db.create_table('tools_paper', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('abstract', self.gf('django.db.models.fields.TextField')()),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tools.Edition'])),
            ('prize', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tools.Prize'], null=True, blank=True)),
            ('tool', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tools.Tool'], null=True, blank=True)),
        ))
        db.send_create_signal('tools', ['Paper'])

        # Adding M2M table for field author on 'Paper'
        db.create_table('tools_paper_author', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('paper', models.ForeignKey(orm['tools.paper'], null=False)),
            ('researcher', models.ForeignKey(orm['tools.researcher'], null=False))
        ))
        db.create_unique('tools_paper_author', ['paper_id', 'researcher_id'])

        # Adding model 'Prize'
        db.create_table('tools_prize', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('place', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('tools', ['Prize'])

        # Adding model 'Tool'
        db.create_table('tools_tool', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('tools', ['Tool'])


    def backwards(self, orm):
        # Deleting model 'Paper'
        db.delete_table('tools_paper')

        # Removing M2M table for field author on 'Paper'
        db.delete_table('tools_paper_author')

        # Deleting model 'Prize'
        db.delete_table('tools_prize')

        # Deleting model 'Tool'
        db.delete_table('tools_tool')


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
        'tools.paper': {
            'Meta': {'object_name': 'Paper'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            'author': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tools.Researcher']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prize': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tools.Prize']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tool': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tools.Tool']", 'null': 'True', 'blank': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tools.Edition']"})
        },
        'tools.prize': {
            'Meta': {'object_name': 'Prize'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tools.researcher': {
            'Meta': {'object_name': 'Researcher'},
            'affiliation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tools.Institution']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tools.tool': {
            'Meta': {'object_name': 'Tool'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['tools']
