# Generated by Django 4.2.2 on 2023-10-15 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Herramientas', '0005_remove_prestamo_cantidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='herramientas',
            name='cantidad',
        ),
    ]
