# Generated by Django 3.0.8 on 2020-07-20 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_delated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='delated',
            new_name='deleted',
        ),
    ]
