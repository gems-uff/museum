# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Paper.title'
        db.alter_column(u'tools_paper', 'title', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'Paper.title'
        db.alter_column(u'tools_paper', 'title', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'tools.edition': {
            'Meta': {'object_name': 'Edition'},
            'chair': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tools.Researcher']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'tools.institution': {
            'Meta': {'object_name': 'Institution'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tools.paper': {
            'Meta': {'object_name': 'Paper'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            'author': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tools.Researcher']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prize': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tools.Prize']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tool': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tools.Tool']", 'null': 'True', 'blank': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tools.Edition']"})
        },
        u'tools.prize': {
            'Meta': {'object_name': 'Prize'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tools.researcher': {
            'Meta': {'object_name': 'Researcher'},
            'affiliation': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tools.Institution']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tools.tool': {
            'Meta': {'object_name': 'Tool'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['tools']