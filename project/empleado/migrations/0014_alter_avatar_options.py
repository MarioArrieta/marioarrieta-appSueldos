# Generated by Django 5.0.4 on 2024-05-18 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0013_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avatar',
            options={'verbose_name': 'Foto de Perfil', 'verbose_name_plural': 'Fotos de Perfiles'},
        ),
    ]
