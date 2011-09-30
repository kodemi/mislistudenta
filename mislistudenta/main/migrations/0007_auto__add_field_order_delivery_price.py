# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Order.delivery_price'
        db.add_column('main_order', 'delivery_price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=9, decimal_places=2), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Order.delivery_price'
        db.delete_column('main_order', 'delivery_price')


    models = {
        'main.book': {
            'Meta': {'object_name': 'Book'},
            'alias': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
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
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Book']"}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders'", 'to': "orm['main.Customer']"}),
            'delivery_method': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'delivery_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_date': ('django.db.models.fields.DateTimeField', [], {}),
            'order_number': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'payment_method': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['main']
