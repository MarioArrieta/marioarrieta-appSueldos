# Generated by Django 5.0.4 on 2024-05-16 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0009_alter_notificaciones_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificaciones',
            name='visto',
            field=models.BooleanField(default=False, verbose_name='Visto'),
        ),
    ]
