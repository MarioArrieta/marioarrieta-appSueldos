# Generated by Django 5.0.4 on 2024-05-11 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0006_alter_notificaciones_visto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificaciones',
            name='archivo_adjunto',
        ),
        migrations.AlterField(
            model_name='notificaciones',
            name='visto',
            field=models.BooleanField(default=False, editable=False, verbose_name='Visto'),
        ),
    ]
