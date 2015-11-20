# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Tatic.chance'
        db.add_column(u'jogo_tatic', 'chance',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Tatic.chance'
        db.delete_column(u'jogo_tatic', 'chance')


    models = {
        u'jogo.exercito': {
            'Meta': {'object_name': 'Exercito'},
            'bandeira': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'cor': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['usuario.Usuario']"})
        },
        u'jogo.soldado': {
            'Meta': {'object_name': 'Soldado'},
            'escudo': ('django.db.models.fields.IntegerField', [], {}),
            'forca': ('django.db.models.fields.IntegerField', [], {}),
            'foto': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'hp': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'max_hp': ('django.db.models.fields.IntegerField', [], {}),
            'mira': ('django.db.models.fields.IntegerField', [], {}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'tatics_defesa': ('django.db.models.fields.IntegerField', [], {}),
            'tatics_estrategia': ('django.db.models.fields.IntegerField', [], {}),
            'tatics_ofensa': ('django.db.models.fields.IntegerField', [], {})
        },
        u'jogo.soldado_tatic': {
            'Meta': {'object_name': 'Soldado_Tatic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'soldado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jogo.Soldado']"}),
            'tatic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jogo.Tatic']"})
        },
        u'jogo.tatic': {
            'Meta': {'object_name': 'Tatic'},
            'chance': ('django.db.models.fields.IntegerField', [], {}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'foto': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'required_defesa': ('django.db.models.fields.IntegerField', [], {}),
            'required_estrategia': ('django.db.models.fields.IntegerField', [], {}),
            'required_ofensa': ('django.db.models.fields.IntegerField', [], {})
        },
        u'usuario.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'senha': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['jogo']