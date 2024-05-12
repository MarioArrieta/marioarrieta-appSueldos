# Generated by Django 5.0.4 on 2024-05-12 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0008_alter_notificaciones_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificaciones',
            name='tipo',
            field=models.CharField(choices=[('1', 'Certificado de enfemedad'), ('2', 'Reclamo'), ('3', 'Permiso Especial'), ('4', 'Solicitud de Vacaciones'), ('5', 'Envío de CBU'), ('6', 'Renuncia'), ('7', 'Otros')], max_length=20, verbose_name='Tipo'),
        ),
    ]
