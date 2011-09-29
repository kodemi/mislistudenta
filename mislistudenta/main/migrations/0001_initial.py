# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Customer'
        db.create_table('main_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('tel', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('main', ['Customer'])

        # Adding model 'Book'
        db.create_table('main_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('main', ['Book'])

        # Adding model 'Order'
        db.create_table('main_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Customer'])),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Book'])),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('payment_method', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('delivery_method', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('main', ['Order'])


    def backwards(self, orm):
        
        # Deleting model 'Customer'
        db.delete_table('main_customer')

        # Deleting model 'Book'
        db.delete_table('main_book')

        # Deleting model 'Order'
        db.delete_table('main_order')


    models = {
        'main.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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
