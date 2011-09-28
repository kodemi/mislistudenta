# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Book.author'
        db.delete_column('main_book', 'author')

        # Adding field 'Book.alias'
        db.add_column('main_book', 'alias', self.gf('django.db.models.fields.CharField')(default='', max_length=64), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Book.author'
        db.add_column('main_book', 'author', self.gf('django.db.models.fields.CharField')(default='', max_length=200), keep_default=False)

        # Deleting field 'Book.alias'
        db.delete_column('main_book', 'alias')


    models = {
        'main.book': {
            'Meta': {'object_name': 'Book'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'main.customer': {
            'Meta': {'object_name': 'Customer'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'main.order': {
            'Meta': {'object_name': 'Order'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Book']"}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Customer']"}),
            'delivery_method': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_method': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['main']
