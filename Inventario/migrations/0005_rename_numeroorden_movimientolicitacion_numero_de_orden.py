# Generated by Django 4.2.2 on 2023-10-23 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0004_movimientolicitacion_numeroorden'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movimientolicitacion',
            old_name='NumeroOrden',
            new_name='Numero_de_Orden',
        ),
    ]
