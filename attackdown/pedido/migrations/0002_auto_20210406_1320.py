# Generated by Django 3.1.7 on 2021-04-06 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='preco',
            new_name='valorTotal',
        ),
    ]