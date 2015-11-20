# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Usuario'
        db.create_table(u'usuario_usuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('senha', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'usuario', ['Usuario'])


    def backwards(self, orm):
        # Deleting model 'Usuario'
        db.delete_table(u'usuario_usuario')


    models = {
        u'usuario.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'senha': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['usuario']