# Generated by Django 4.1.2 on 2022-11-26 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='cedula',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='email',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='valor',
        ),
    ]