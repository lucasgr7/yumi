# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Exercito'
        db.create_table(u'jogo_exercito', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('slogan', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('bandeira', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('cor', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['usuario.Usuario'])),
        ))
        db.send_create_signal(u'jogo', ['Exercito'])

        # Adding model 'Soldado'
        db.create_table(u'jogo_soldado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('foto', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('forca', self.gf('django.db.models.fields.IntegerField')()),
            ('escudo', self.gf('django.db.models.fields.IntegerField')()),
            ('mira', self.gf('django.db.models.fields.IntegerField')()),
            ('max_hp', self.gf('django.db.models.fields.IntegerField')()),
            ('hp', self.gf('django.db.models.fields.IntegerField')()),
            ('tatics_ofensa', self.gf('django.db.models.fields.IntegerField')()),
            ('tatics_defesa', self.gf('django.db.models.fields.IntegerField')()),
            ('tatics_estrategia', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'jogo', ['Soldado'])

        # Adding model 'Tatic'
        db.create_table(u'jogo_tatic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('foto', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('required_ofensa', self.gf('django.db.models.fields.IntegerField')()),
            ('required_defesa', self.gf('django.db.models.fields.IntegerField')()),
            ('required_estrategia', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'jogo', ['Tatic'])

        # Adding model 'Soldado_Tatic'
        db.create_table(u'jogo_soldado_tatic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('soldado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jogo.Soldado'])),
            ('tatic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jogo.Tatic'])),
        ))
        db.send_create_signal(u'jogo', ['Soldado_Tatic'])


    def backwards(self, orm):
        # Deleting model 'Exercito'
        db.delete_table(u'jogo_exercito')

        # Deleting model 'Soldado'
        db.delete_table(u'jogo_soldado')

        # Deleting model 'Tatic'
        db.delete_table(u'jogo_tatic')

        # Deleting model 'Soldado_Tatic'
        db.delete_table(u'jogo_soldado_tatic')


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