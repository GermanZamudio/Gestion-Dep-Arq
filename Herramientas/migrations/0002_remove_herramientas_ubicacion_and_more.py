# Generated by Django 4.2.2 on 2023-07-03 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Herramientas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='herramientas',
            name='ubicacion',
        ),
        migrations.DeleteModel(
            name='Acta_entrega_herramienta',
        ),
        migrations.DeleteModel(
            name='Herramientas',
        ),
    ]