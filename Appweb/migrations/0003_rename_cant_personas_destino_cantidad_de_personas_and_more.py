# Generated by Django 4.0.3 on 2022-04-13 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appweb', '0002_rename_hotel_alojamiento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destino',
            old_name='cant_personas',
            new_name='cantidad_de_personas',
        ),
        migrations.RenameField(
            model_name='pasajero',
            old_name='mail',
            new_name='email',
        ),
    ]