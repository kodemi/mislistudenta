# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Order.order_date'
        db.add_column('main_order', 'order_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 9, 28, 3, 25, 40, 284609)), keep_default=False)

        # Adding field 'Order.order_number'
        db.add_column('main_order', 'order_number', self.gf('django.db.models.fields.CharField')(default='', max_length=6), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Order.order_date'
        db.delete_column('main_order', 'order_date')

        # Deleting field 'Order.order_number'
        db.delete_column('main_order', 'order_number')


    models = {
        'main.book': {
            'Meta': {'object_name': 'Book'},
            'alias': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
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
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders'", 'to': "orm['main.Customer']"}),
            'delivery_method': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_date': ('django.db.models.fields.DateTimeField', [], {}),
            'order_number': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'payment_method': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['main']
